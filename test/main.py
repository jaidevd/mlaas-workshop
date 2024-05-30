from sklearn.linear_model import LogisticRegression
from sklearn.utils import estimator_html_repr


def default(handler):
    return estimator_html_repr(LogisticRegression())
