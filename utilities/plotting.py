import shap
import pandas as pd
from pdpbox import pdp
import matplotlib.pyplot as plt


def plot_feature_importance(model, data: pd.DataFrame, **kwargs):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(data)
    return shap.summary_plot(shap_values, data, plot_type='bar', plot_size=(14, 10), **kwargs)


def partial_dependence_plot(model, data: pd.DataFrame, model_features: list, column: str):
    pdp_df = pdp.pdp_isolate(model=model, dataset=data, model_features=model_features, feature=column)
    pdp.pdp_plot(pdp_df, column, figsize=(10, 8))
    return plt.show()
