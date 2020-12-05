import joblib
import logging
import pandas as pd
import config.config as cfg

logger = logging.getLogger(cfg.logger_app_name)


def save_model(model, filepath: str):
    joblib.dump(model, filename=filepath)
    logger.info('El modelo se ha guardado correctamente.')
    return True


def load_model(filepath: str):
    model = joblib.load(filename=filepath)
    logger.info('El modelo se ha cargado correctamente.')
    return model


def prediction(data: pd.DataFrame, model):
    data['probability'] = model.predict_proba(data)[:, 1]
    return data
