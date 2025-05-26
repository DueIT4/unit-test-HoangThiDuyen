from typing import List


class StudentAnalyzer:
    def count_excellent_students(self, scores: List[float]) -> int:
        return sum(1 for score in scores if 8.0 <= score <= 10.0)

    def calculate_valid_average(self, scores: List[float]) -> float:
        valid_scores = [score for score in scores if 0.0 <= score <= 10.0]
        return sum(valid_scores) / len(valid_scores) if valid_scores else 0.0
