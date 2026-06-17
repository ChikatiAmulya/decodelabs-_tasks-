from dataset import courses


def get_recommendations(user_interests):
    recommendations = []

    user_interests = [
        interest.strip().lower()
        for interest in user_interests
    ]

    for course in courses:
        course_tags = [
            tag.lower()
            for tag in course["tags"]
        ]

        match_score = 0

        for interest in user_interests:
            if interest in course_tags:
                match_score += 1

        recommendations.append({
            "name": course["name"],
            "score": match_score
        })

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations


def display_interests():
    interests = set()

    for course in courses:
        for tag in course["tags"]:
            interests.add(tag)

    print("\nAvailable Interests:")
    print("-" * 30)

    for interest in sorted(interests):
        print(interest)


def main():
    print("=" * 60)
    print("        AI RECOMMENDATION SYSTEM")
    print("=" * 60)

    while True:
        print("\nMENU")
        print("1. Get Recommendations")
        print("2. View Available Interests")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            user_input = input(
                "\nEnter your interests (comma separated): "
            )

            user_interests = user_input.split(",")

            recommendations = get_recommendations(user_interests)

            print("\nRecommended Courses")
            print("-" * 30)

            found = False

            for item in recommendations:
                if item["score"] > 0:
                    found = True
                    print(
                        f"{item['name']} "
                        f"(Match Score: {item['score']})"
                    )

            if not found:
                print("No matching recommendations found.")

        elif choice == "2":
            display_interests()

        elif choice == "3":
            print("\nThank you for using the AI Recommendation System.")
            print("Project completed successfully.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()