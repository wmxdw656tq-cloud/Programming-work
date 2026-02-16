
def calculate_spam_score(message, spam_terms):
    """
    Scans the message for spam terms.
    Returns: (score, matched_terms_dict)
    """
    message_lower = message.lower()
    score = 0
    matched_terms = {}

    for term in spam_terms:
        term_lower = term.lower()
        count = message_lower.count(term_lower)
        if count > 0:
            score += count
            matched_terms[term] = count

    return score, matched_terms


def rate_spam_likelihood(score):
    """
    Rates the likelihood of spam based on score.
    """
    if score == 0:
        return "Very unlikely to be spam"
    elif 1 <= score <= 3:
        return "Unlikely to be spam"
    elif 4 <= score <= 7:
        return "Possibly spam"
    elif 8 <= score <= 12:
        return "Likely spam"
    else:
        return "Very likely spam"


def main():
    spam_terms = [
        "free", "winner", "congratulations", "act now", "limited time", "urgent",
        "risk-free", "guaranteed", "no obligation", "click here", "click now",
        "buy now", "order now", "money-back", "earn money", "work from home",
        "investment opportunity", "no credit check", "lowest price", "cheap",
        "credit card", "winner!", "you have been selected", "act immediately",
        "call now", "100% free", "no fees", "get paid", "extra income",
        "limited offer"
    ]

    print("=== Spam Checker ===")
    message = input("Enter your email message:\n")

    score, matched_terms = calculate_spam_score(message, spam_terms)
    likelihood = rate_spam_likelihood(score)

    print("\n=== Results ===")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")

    if matched_terms:
        print("\nSpam-triggering words/phrases found:")
        for term, count in matched_terms.items():
            print(f" - '{term}' occurred {count} time(s)")
    else:
        print("\nNo spam terms were found in the message.")


if __name__ == "__main__":
    main()
