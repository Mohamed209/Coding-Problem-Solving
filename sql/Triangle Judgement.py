#https://leetcode.com/problems/triangle-judgement/description/
import pandas as pd

data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=["x", "y", "z"]).astype(
    {"x": "Int64", "y": "Int64", "z": "Int64"}
)


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def judge(x, y, z):
        return "Yes" if x + y > z and x + z > y and y + z > x else "No"

    triangle["triangle"] = triangle.apply(lambda row: judge(*row), axis=1)
    return triangle


print(triangle_judgement(triangle))
