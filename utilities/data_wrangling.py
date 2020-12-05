import logging
import pandas as pd
import config.config as cfg
from sklearn.model_selection import train_test_split

logger = logging.getLogger(cfg.logger_app_name)


def load_data(filepath: str, **kwargs) -> pd.DataFrame:
    dataframe = pd.read_csv(filepath, **kwargs)
    logger.info('Se han cargado los datos correctamente.')
    return dataframe


def split_dataset(df: pd.DataFrame, label: str, stratify: bool = False):
    target = df.pop(label)
    if stratify:
        train_data, test_data, train_label, test_label = train_test_split(df, target, test_size=0.3,
                                                                          random_state=cfg.SEED, stratify=target)
    else:
        train_data, test_data, train_label, test_label = train_test_split(df, target, test_size=0.3,
                                                                          random_state=cfg.SEED)
    logger.info('Se ha partido el conjunto de datos en conjuntos de entrenamiento, validacion, y prueba.')
    return train_data, test_data, train_label, test_label


def export_data(df: pd.DataFrame, filepath: str, **kwargs):
    logger.info('El archivo se ha exportado como un csv satisfactoriamente.')
    return df.to_csv(filepath, sep=';', index=False, **kwargs)
