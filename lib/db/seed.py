from lib.models.author import Author
from lib.models.magazine import Magazine

def seed():
    a1 = Author("Alice")
    a1.save()
    a2 = Author("Bob")
    a2.save()

    m1 = Magazine("Tech World", "Technology")
    m1.save()
    m2 = Magazine("Health First", "Health")
    m2.save()

    a1.add_article(m1, "The Rise of AI")
    a1.add_article(m2, "Healthy Habits")
    a2.add_article(m1, "Cybersecurity Today")
    a2.add_article(m1, "Cloud Computing")
    a2.add_article(m1, "Edge AI")

    print("Database seeded.")

if __name__ == "__main__":
    seed()
