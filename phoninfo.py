B

    ��]�  �               @   sX   d dl mZ d dlZd dlZd dlmZmZmZ eedd�� ed� dd� Ze�  dS )	�    )�coloredN)�geocoder�timezone�carrierzl
	     WELCOME TO BANgLADESH
                ==============
	          BANgLADESH
                     V1.O
�greenz
 Example(+xx1234567890)c                 s�   x�t tdd��� t tdd��} | dkr0t�d� | dkrHttdd�� nttd	| � d
�d�� P t�� �}t�|d�}ttdd
�|� � fdd�}|�  � fdd�}|�  qW d S )Nz   Enter number: ZbluezContinue ? Y/n: Zred�nz
 Shutting down... �yz
 Target Number... 
z
  Invalid 'z'  Try again ! 
�enz	Country: r   c                 s*   t �� �} t�| d�}ttdd�|� d S )Nr	   zISP: r   )�phonenumbers�parser   Zname_for_number�printr   )�i�s)�b� �3/data/data/com.termux/files/home/phone.pyp/phone.py�isp)   s    
zinfo.<locals>.ispc                 s*   t �� �} t�| �}ttdd�|d� d S )Nz
Timezone: r   �
)r
   r   r   Ztime_zones_for_numberr   r   )�p�e)r   r   r   �time.   s    

zinfo.<locals>.time)	�inputr   �sys�exitr   r
   r   r   Zdescription_for_number)Zinp�exZexpr   r   r   )r   r   �info   s     

r   )	Z	termcolorr   r
   r   r   r   r   r   r   r   r   r   r   �<module>   s   
&
