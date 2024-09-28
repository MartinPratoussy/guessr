genres_dict = {
    'Thrash Metal': {
        'features': {
            'tempo': (150, 220),  # Fast tempo
            'energy': (0.7, 1.0),  # Very energetic
            'valence': (0.3, 0.7),  # Medium to dark emotional tone
            'instrumentalness': (0.0, 0.3),  # Low instrumental
            'loudness': (-5.0, 0.0),  # Loud sound
            'speechiness': (0.03, 0.1),  # Low speech content
        },
        'weights': {
            'tempo': 2.0,  # High weight on tempo
            'energy': 1.5,  # Energy is also key
            'valence': 1.0,
            'instrumentalness': 0.5,
            'loudness': 1.5,
            'speechiness': 0.5,
        }
    },
    'Doom Metal': {
        'features': {
            'tempo': (60, 90),  # Slow tempo
            'energy': (0.2, 0.5),  # Low energy
            'valence': (0.1, 0.4),  # Very dark emotional tone
            'instrumentalness': (0.3, 0.7),  # Can be more instrumental
            'loudness': (-10.0, -5.0),  # Not extremely loud
            'acousticness': (0.1, 0.4),  # Can have some acoustic elements
        },
        'weights': {
            'tempo': 1.5,  # Tempo is important but not dominant
            'energy': 2.0,  # Low energy is a signature of Doom Metal
            'valence': 1.5,
            'instrumentalness': 1.0,
            'loudness': 1.0,
            'acousticness': 0.5,
        }
    },
    'Death Metal': {
        'features': {
            'tempo': (120, 200),  # Fast tempo
            'energy': (0.8, 1.0),  # High energy
            'valence': (0.1, 0.4),  # Dark and aggressive
            'instrumentalness': (0.0, 0.2),  # Minimal instrumental
            'loudness': (-6.0, 0.0),  # Very loud
            'speechiness': (0.04, 0.08),  # Some growled vocals, but not speech-like
        },
        'weights': {
            'tempo': 1.5,
            'energy': 2.0,  # Energy is very important
            'valence': 1.0,
            'instrumentalness': 0.5,
            'loudness': 1.5,
            'speechiness': 1.0,
        }
    },
    'Hardcore Punk': {
        'features': {
            'tempo': (180, 250),  # Very fast tempo
            'energy': (0.8, 1.0),  # Very energetic
            'valence': (0.4, 0.7),  # More positive
            'instrumentalness': (0.0, 0.2),  # Minimal instrumental sections
            'loudness': (-5.0, 0.0),  # Loud
            'speechiness': (0.05, 0.15),  # More spoken vocals
        },
        'weights': {
            'tempo': 2.0,
            'energy': 1.5,
            'valence': 1.0,
            'instrumentalness': 0.5,
            'loudness': 1.0,
            'speechiness': 1.0,
        }
    },
    'Metalcore': {
        'features': {
            'tempo': (120, 180),  # Medium to fast tempo
            'energy': (0.6, 0.9),  # Energetic
            'valence': (0.2, 0.6),  # Varies
            'instrumentalness': (0.0, 0.3),  # Limited instrumental
            'loudness': (-6.0, 0.0),  # Loud
            'acousticness': (0.0, 0.2),  # Rarely acoustic
        },
        'weights': {
            'tempo': 1.5,
            'energy': 1.5,
            'valence': 1.0,
            'instrumentalness': 0.5,
            'loudness': 1.0,
            'acousticness': 0.5,
        }
    },
    'Power Metal': {
        'features': {
            'tempo': (130, 200),  # Fast tempo
            'energy': (0.7, 1.0),  # Very energetic
            'valence': (0.6, 0.9),  # Bright, positive
            'instrumentalness': (0.0, 0.2),  # Very vocal-driven
            'loudness': (-5.0, 0.0),  # Loud
            'acousticness': (0.0, 0.3),  # Rare acoustic sections
        },
        'weights': {
            'tempo': 2.0,
            'energy': 1.5,
            'valence': 1.5,  # Positivity is key in Power Metal
            'instrumentalness': 0.5,
            'loudness': 1.0,
            'acousticness': 0.5,
        }
    },
    'Deathcore': {
        'features': {
            'tempo': (120, 200),  # Fast tempo
            'energy': (0.8, 1.0),  # High energy
            'valence': (0.1, 0.4),  # Dark and aggressive
            'instrumentalness': (0.0, 0.2),  # Minimal instrumental sections
            'loudness': (-6.0, 0.0),  # Very loud
            'speechiness': (0.04, 0.08),  # Some vocals are more spoken
        },
        'weights': {
            'tempo': 1.5,
            'energy': 2.0,  # High energy is a signature
            'valence': 1.0,
            'instrumentalness': 0.5,
            'loudness': 1.5,
            'speechiness': 1.0,
        }
    },
    'Black Metal': {
        'features': {
            'tempo': (110, 200),  # Fast tempo
            'energy': (0.6, 0.9),  # Intense energy
            'valence': (0.0, 0.3),  # Dark tone
            'instrumentalness': (0.2, 0.5),  # Can be quite instrumental
            'loudness': (-8.0, -3.0),  # Often not as loud as Death Metal
            'acousticness': (0.0, 0.2),  # Rare acoustic elements
        },
        'weights': {
            'tempo': 1.5,
            'energy': 1.5,
            'valence': 2.0,  # Darkness is very important in Black Metal
            'instrumentalness': 1.0,
            'loudness': 1.0,
            'acousticness': 0.5,
        }
    },
    'Progressive Metal': {
        'features': {
            'tempo': (80, 160),  # Variable tempo
            'energy': (0.4, 0.8),  # Can vary greatly
            'valence': (0.3, 0.7),  # Emotional range varies
            'instrumentalness': (0.3, 0.7),  # High instrumental content
            'loudness': (-6.0, 0.0),  # Can be loud but dynamic
            'time_signature': (3, 7),  # Unusual time signatures
        },
        'weights': {
            'tempo': 1.0,
            'energy': 1.0,
            'valence': 1.0,
            'instrumentalness': 2.0,  # Instrumental complexity is key
            'loudness': 1.0,
            'time_signature': 2.0,  # Unique rhythms are very important
        }
    },
    'Alternative Metal': {
        'features': {
            'tempo': (100, 160),  # Moderate tempo
            'energy': (0.5, 0.8),  # Energetic but not extreme
            'valence': (0.3, 0.7),  # Emotional range varies
            'instrumentalness': (0.0, 0.4),  # Limited instrumental sections
            'loudness': (-8.0, -3.0),  # Moderately loud
            'acousticness': (0.0, 0.2),  # Few acoustic elements
        },
        'weights': {
            'tempo': 1.0,
            'energy': 1.5,
            'valence': 1.0,
            'instrumentalness': 0.5,
            'loudness': 1.0,
            'acousticness': 0.5,
        }
    },
    'Djent': {
        'features': {
            'tempo': (120, 180),  # Medium to fast tempo
            'energy': (0.6, 0.9),  # Highly energetic
            'valence': (0.2, 0.6),  # Can vary but often a bit dark
            'instrumentalness': (0.3, 0.7),  # Often has complex instrumental sections
            'loudness': (-6.0, 0.0),  # Loud but dynamic
            'time_signature': (4, 8),  # Complex time signatures are key to Djent
            'acousticness': (0.0, 0.3),  # Mostly electric but occasionally some acoustic
        },
        'weights': {
            'tempo': 1.5,
            'energy': 1.5,
            'valence': 1.0,
            'instrumentalness': 2.0,  # Instrumental sections are crucial
            'loudness': 1.0,
            'time_signature': 2.0,  # High importance on complex rhythms
            'acousticness': 0.5,
        }
    }
}