import requests
import base64
import genres

def getAccessToken():
    client_id = "1d8162e61a994af9a2519f7ff6f4f33e"
    client_secret = "a928e2ffe22845978768ac70aeee5351"
    auth_string = auth_string = f"{client_id}:{client_secret}"
    b64_auth_string = base64.b64encode(auth_string.encode()).decode()
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {b64_auth_string}",
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)
    token_info = response.json()
    access_token = token_info['access_token']
        
    return access_token

def getTrackFeatures(song_id, access_token):
    headers = { 'Authorization': 'Bearer ' + access_token }
    url = f'https://api.spotify.com/v1/audio-features/{song_id}'
    response = requests.get(url, headers=headers)
    return response.json()

def calculateGenreScore(audio_features, genre_profile):
    # Extract the features and weights for the genre
    genre_features = genre_profile['features']
    genre_weights = genre_profile['weights']

    # Calculate the total weight for normalization later
    total_weight = sum(genre_weights.values())

    score = 0
    
    # Loop through each feature in the genre's profile
    for key, (min_val, max_val) in genre_features.items():
        feature_value = audio_features.get(key)
        
        if feature_value is not None:
            # Calculate the center of the range and the span
            center = (min_val + max_val) / 2
            range_span = max_val - min_val
            
            # Calculate proximity to the center (closer = higher score)
            proximity = max(0, 1 - abs(feature_value - center) / (range_span / 2))
            
            # Add to the score, applying the corresponding weight
            score += proximity * genre_weights.get(key, 1)
    
    # Normalize the score by the total weight
    return (score / total_weight) * 100

def main():
    track_features = getTrackFeatures("2l0h4aBFLp9HdoaNdCTlbW", getAccessToken())
    track_score = {}
    for genre, profile in genres.genres_dict.items():
        score = calculateGenreScore(track_features, profile)
        track_score[genre] = score
    for genre, score in sorted(track_score.items(), key=lambda item: item[1], reverse=True):
        print(f'{genre}: {score:.2f}%')
    
if __name__ == "__main__":
    main()
