from array import array
import os

def unique(items):
    prev = None
    for item in items:
        if prev is None or prev != item:
            yield item
        prev = item

def climbingLeaderboard(scores, alice):
    unique_alice = array("i", list(unique(alice))[::-1])
    unique_scores = array("i", list(unique(scores)))
    alice_ranks = dict()
    last_rank = 1
    for alice_score in unique_alice:
        for idx, score in enumerate(unique_scores):
            if alice_score >= score:
                alice_ranks[alice_score] = last_rank + idx
                last_rank += idx
                break
        else:
            alice_ranks[alice_score] = last_rank + len(unique_scores)
            last_rank += len(unique_scores)
            idx += 1
        unique_scores = unique_scores[idx:]

    return [alice_ranks[score] for score in alice]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))
    # print(min(scores), max(alice))
    # print(len(list(unique(scores))))
    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
