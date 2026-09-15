from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    #initialize best score and best name 
    best_score, best_name = 0,""

    #unpack score into name and score 
    for name,score in scores:
        #check if the score being looped on is greaters then the current best score 
        if score > best_score:
            #if so set the best score to the score and the best name to name 
            best_score, best_name = score,name
    #return the best name 
    return best_name

        


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
