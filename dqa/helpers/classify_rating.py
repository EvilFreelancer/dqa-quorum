import json
import statistics


def classify_rating(ratings_by_experts: list, quorum: int):
    classified_samples = []

    for i, ratings in enumerate(ratings_by_experts):

        # Skip empty ratings
        if ratings is None:
            continue

        # Count the number of valid (non-None) ratings
        valid_ratings = [rating for rating in ratings.values() if rating is not None]

        # Check if the number of valid ratings meets or exceeds the quorum
        majority_vote = True
        if len(valid_ratings) < quorum:
            majority_vote = False
            print(f"Sample {i + 1}: Not enough valid ratings. Skipping classification.")

        # Calculate the average rating
        average_rating = statistics.mean(valid_ratings)
        classification = "Good" if average_rating > 3.5 else "Bad"

        # Check for a majority vote
        print(f"Sample {i + 1}: AVG Rating: {average_rating}, Class: {classification}")
        print(f"Ratings: {json.dumps(valid_ratings)}")
        print(f"Majority Vote Achieved: {majority_vote}")
        print(f"")

        classified_samples.append({
            "sample_index": i + 1,
            "average_rating": average_rating,
            "classification": classification,
            "majority_vote": majority_vote
        })

    return classified_samples if classified_samples else None

