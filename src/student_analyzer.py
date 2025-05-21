from typing import List

class StudentAnalyzer:
    def countExcellentStudents(self, scores: List[float]) -> int:
        if not scores:
            return 0
        count = 0
        for score in scores:
            if 0 <= score <= 10 and score >= 8.0:
                count += 1
        return count
