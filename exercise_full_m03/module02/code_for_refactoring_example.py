'''
NovaBrain平台用户数据处理模块
功能：处理用户上传的数据，进行清洗、转换和基本统计
'''

import pandas as pd
import numpy as np
import os
import json
import logging
from datetime import datetime

# 全局变量
VALID_FILE_TYPES = ['csv', 'json', 'txt']
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
LOG_FILE = "data_processing.log"

# 初始化日志
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def check_file(file_path):
    """
    检查文件是否符合要求
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        logging.error(f"文件不存在: {file_path}")
        return False
    
    # 检查文件大小
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE:
        logging.error(f"文件大小超过限制: {file_size} > {MAX_FILE_SIZE}")
        return False
    
    # 检查文件类型
    file_ext = file_path.split('.')[-1].lower()
    if file_ext not in VALID_FILE_TYPES:
        logging.error(f"不支持的文件类型: {file_ext}")
        return False
    
    return True

def load_data(file_path):
    """
    根据文件类型加载数据
    """
    file_ext = file_path.split('.')[-1].lower()
    
    try:
        if file_ext == 'csv':
            data = pd.read_csv(file_path)
            logging.info(f"成功加载CSV文件: {file_path}")
            return data
        elif file_ext == 'json':
            data = pd.read_json(file_path)
            logging.info(f"成功加载JSON文件: {file_path}")
            return data
        elif file_ext == 'txt':
            with open(file_path, 'r') as f:
                lines = f.readlines()
            data = pd.DataFrame({'text': lines})
            logging.info(f"成功加载TXT文件: {file_path}")
            return data
    except Exception as e:
        logging.error(f"加载文件失败: {str(e)}")
        return None

def process_numerical_data(data, columns):
    """
    处理数值型数据
    """
    results = {}
    
    for col in columns:
        if col in data.columns and pd.api.types.is_numeric_dtype(data[col]):
            col_data = data[col].dropna()
            
            # 计算基本统计量
            mean_val = col_data.mean()
            median_val = col_data.median()
            std_val = col_data.std()
            min_val = col_data.min()
            max_val = col_data.max()
            
            # 存储结果
            results[col] = {
                'mean': mean_val,
                'median': median_val,
                'std': std_val,
                'min': min_val,
                'max': max_val,
                'missing_count': data[col].isna().sum(),
                'missing_percent': data[col].isna().sum() / len(data) * 100
            }
            
            logging.info(f"完成数值列处理: {col}")
        else:
            logging.warning(f"列不存在或非数值类型: {col}")
    
    return results

def process_categorical_data(data, columns):
    """
    处理类别型数据
    """
    results = {}
    
    for col in columns:
        if col in data.columns:
            col_data = data[col].dropna()
            
            # 计算类别统计
            value_counts = col_data.value_counts()
            unique_count = len(value_counts)
            most_common = value_counts.index[0] if not value_counts.empty else None
            most_common_count = value_counts.iloc[0] if not value_counts.empty else 0
            
            # 存储结果
            results[col] = {
                'unique_count': unique_count,
                'most_common': most_common,
                'most_common_count': most_common_count,
                'missing_count': data[col].isna().sum(),
                'missing_percent': data[col].isna().sum() / len(data) * 100,
                'distribution': value_counts.to_dict() if unique_count < 10 else None
            }
            
            logging.info(f"完成类别列处理: {col}")
        else:
            logging.warning(f"列不存在: {col}")
    
    return results

def process_text_data(data, columns):
    """
    处理文本数据
    """
    results = {}
    
    for col in columns:
        if col in data.columns:
            col_data = data[col].dropna().astype(str)
            
            # 计算文本统计
            avg_length = col_data.str.len().mean()
            max_length = col_data.str.len().max()
            min_length = col_data.str.len().min()
            
            # 存储结果
            results[col] = {
                'avg_length': avg_length,
                'max_length': max_length,
                'min_length': min_length,
                'missing_count': data[col].isna().sum(),
                'missing_percent': data[col].isna().sum() / len(data) * 100
            }
            
            logging.info(f"完成文本列处理: {col}")
        else:
            logging.warning(f"列不存在: {col}")
    
    return results

def clean_data(data, rules):
    """
    根据规则清洗数据
    """
    cleaned_data = data.copy()
    
    for rule in rules:
        column = rule.get('column')
        action = rule.get('action')
        
        if column not in cleaned_data.columns:
            logging.warning(f"清洗规则中的列不存在: {column}")
            continue
        
        # 处理缺失值
        if action == 'drop_na':
            cleaned_data = cleaned_data.dropna(subset=[column])
            logging.info(f"删除列 {column} 中的缺失值")
        
        elif action == 'fill_na_mean' and pd.api.types.is_numeric_dtype(cleaned_data[column]):
            mean_val = cleaned_data[column].mean()
            cleaned_data[column] = cleaned_data[column].fillna(mean_val)
            logging.info(f"用均值填充列 {column} 中的缺失值")
        
        elif action == 'fill_na_median' and pd.api.types.is_numeric_dtype(cleaned_data[column]):
            median_val = cleaned_data[column].median()
            cleaned_data[column] = cleaned_data[column].fillna(median_val)
            logging.info(f"用中位数填充列 {column} 中的缺失值")
        
        elif action == 'fill_na_mode':
            mode_val = cleaned_data[column].mode()[0]
            cleaned_data[column] = cleaned_data[column].fillna(mode_val)
            logging.info(f"用众数填充列 {column} 中的缺失值")
        
        elif action == 'fill_na_value':
            value = rule.get('value')
            cleaned_data[column] = cleaned_data[column].fillna(value)
            logging.info(f"用指定值 {value} 填充列 {column} 中的缺失值")
        
        # 过滤数据
        elif action == 'filter_greater_than' and pd.api.types.is_numeric_dtype(cleaned_data[column]):
            threshold = rule.get('threshold')
            cleaned_data = cleaned_data[cleaned_data[column] > threshold]
            logging.info(f"过滤列 {column} 中大于 {threshold} 的值")
        
        elif action == 'filter_less_than' and pd.api.types.is_numeric_dtype(cleaned_data[column]):
            threshold = rule.get('threshold')
            cleaned_data = cleaned_data[cleaned_data[column] < threshold]
            logging.info(f"过滤列 {column} 中小于 {threshold} 的值")
        
        elif action == 'filter_equals':
            value = rule.get('value')
            cleaned_data = cleaned_data[cleaned_data[column] == value]
            logging.info(f"过滤列 {column} 中等于 {value} 的值")
        
        # 转换数据
        elif action == 'to_lowercase' and pd.api.types.is_string_dtype(cleaned_data[column]):
            cleaned_data[column] = cleaned_data[column].str.lower()
            logging.info(f"将列 {column} 中的文本转换为小写")
        
        elif action == 'to_uppercase' and pd.api.types.is_string_dtype(cleaned_data[column]):
            cleaned_data[column] = cleaned_data[column].str.upper()
            logging.info(f"将列 {column} 中的文本转换为大写")
    
    return cleaned_data

def save_processed_data(data, output_path, file_format):
    """
    保存处理后的数据
    """
    try:
        if file_format == 'csv':
            data.to_csv(output_path, index=False)
        elif file_format == 'json':
            data.to_json(output_path, orient='records')
        elif file_format == 'excel':
            data.to_excel(output_path, index=False)
        else:
            logging.error(f"不支持的输出格式: {file_format}")
            return False
        
        logging.info(f"成功保存数据到: {output_path}")
        return True
    except Exception as e:
        logging.error(f"保存数据失败: {str(e)}")
        return False

def save_summary_report(numerical_results, categorical_results, text_results, output_path):
    """
    保存数据摘要报告
    """
    summary = {
        'generated_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'numerical_features': numerical_results,
        'categorical_features': categorical_results,
        'text_features': text_results
    }
    
    try:
        with open(output_path, 'w') as f:
            json.dump(summary, f, indent=4)
        
        logging.info(f"成功保存摘要报告到: {output_path}")
        return True
    except Exception as e:
        logging.error(f"保存摘要报告失败: {str(e)}")
        return False

def main_processing_function(file_path, output_directory, clean_rules=None):
    """
    主处理函数
    """
    # 检查文件
    if not check_file(file_path):
        return False, "文件检查失败"
    
    # 加载数据
    data = load_data(file_path)
    if data is None:
        return False, "数据加载失败"
    
    # 数据基本信息
    rows, cols = data.shape
    logging.info(f"数据维度: {rows} 行 × {cols} 列")
    
    # 分类各种列
    numerical_columns = []
    categorical_columns = []
    text_columns = []
    
    for col in data.columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            numerical_columns.append(col)
        elif pd.api.types.is_string_dtype(data[col]) and data[col].str.len().mean() > 50:
            text_columns.append(col)
        else:
            categorical_columns.append(col)
    
    logging.info(f"数值列: {len(numerical_columns)}, 类别列: {len(categorical_columns)}, 文本列: {len(text_columns)}")
    
    # 数据处理
    numerical_results = process_numerical_data(data, numerical_columns)
    categorical_results = process_categorical_data(data, categorical_columns)
    text_results = process_text_data(data, text_columns)
    
    # 数据清洗
    if clean_rules:
        cleaned_data = clean_data(data, clean_rules)
        logging.info(f"清洗后数据维度: {cleaned_data.shape[0]} 行 × {cleaned_data.shape[1]} 列")
    else:
        cleaned_data = data
        logging.info("未应用清洗规则")
    
    # 创建输出目录
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        logging.info(f"创建输出目录: {output_directory}")
    
    # 保存处理后的数据
    output_file = os.path.join(output_directory, "processed_data.csv")
    if not save_processed_data(cleaned_data, output_file, 'csv'):
        return False, "保存处理后的数据失败"
    
    # 保存摘要报告
    summary_file = os.path.join(output_directory, "data_summary.json")
    if not save_summary_report(numerical_results, categorical_results, text_results, summary_file):
        return False, "保存摘要报告失败"
    
    return True, "处理完成"

# 示例用法
if __name__ == "__main__":
    # 示例清洗规则
    sample_rules = [
        {'column': 'age', 'action': 'fill_na_median'},
        {'column': 'income', 'action': 'filter_greater_than', 'threshold': 0},
        {'column': 'name', 'action': 'to_uppercase'}
    ]
    
    success, message = main_processing_function(
        file_path="sample_data.csv",
        output_directory="./output",
        clean_rules=sample_rules
    )
    
    print(f"处理结果: {message}") 