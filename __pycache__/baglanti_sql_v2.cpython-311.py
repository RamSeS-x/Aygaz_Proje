�
    ��ed�  �                   �   � d dl mZ  e�   �         Zd dlZd dlZd dlZ ej        �   �           ej        d�  �        Z	 ej        d�  �        Z
d� ZdS )�    )�connect_to_githubN�
SQL_SERVER�DB_NAMEc                  �  � dt           � dt          � d�} 	 t          j        | �  �        }|�                    �   �         }t          d�  �         n@# t          j        j        $ r)}t          dt          |�  �        z   �  �         Y d }~nd }~ww xY w|S )Nzmssql+pyodbc://�/z<?driver=SQL+Server+Native+Client+11.0&Trusted_Connection=yesu   Bağlantı başarılıu   Bağlantı başarısız: )	r   r   �sa�create_engine�connect�print�exc�SQLAlchemyError�str)�conn_str�engine�
connection�exs       �FC:\Users\Mehmet Keskin\Documents\GitHub\Aygaz_proje\baglanti_sql_v2.py�baglanti_sql_v2r   #   s�   � �	"�*� 	"� 	"�w� 	"� 	"� 	"� �5��!�(�+�+���^�^�%�%�
��&�'�'�'�'���6�!� 5� 5� 5��)�C��G�G�3�4�4�4�4�4�4�4�4�����5���� �Ms   �7A �B
�!B�B
)�repository_baglanr   �repo�os�
sqlalchemyr   �dotenv�load_dotenv�getenvr   r   r   � �    r   �<module>r      s�   ��( 0� /� /� /� /� /������
 
�	�	�	� � � � � ���� �� � � � ��R�Y�|�$�$�
�
�"�)�I�
�
��� � � � r   