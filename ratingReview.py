def ratingReview(threshold, ratings):
    r = []
    for i in range(len(ratings)):
        c = ratings[i]
        if sum(c) / len(c) < threshold:
            r.append(i)
    return r
