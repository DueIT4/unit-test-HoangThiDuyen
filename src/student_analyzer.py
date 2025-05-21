from typing import List

class student_analyzer:
    def count_excellent_students(self, scores: List[float]) -> int:
        if not scores:
            return 0
        count = 0
        for score in scores:
            if 0 <= score <= 10 and score >= 8.0:
                count += 1
        return count


    def calculate_valid_average(self, scores: List[float]) -> float:
        if not scores:
            return 0.0
        valid_scores = [score for score in scores if 0 <= score <= 10]
        if not valid_scores:
            return 0.0
        return sum(valid_scores) / len(valid_scores)
