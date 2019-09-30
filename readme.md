# Administrador base datos - IN3501

Programa creado para realizar queries en lenguaje SQL para el curso IN305. En la imagen _modelo_er.png_ se encuentra el modelo entidad relacion de la base de datos utilizada

### Prerequisitos

Debes tener instalado: 
* **Python3** (con pip)
* **Entorno virtual**: no es necesario, pero es recomendado.


### Instalaciones

Crear un entorno virtual, activarlo y luego instalar los requerimientos:


```
pip install -r requirements.txt
```

## Como usar el programa:

Para iniciar el programa debes ejecutar:
```
python queries.py
```

Ahora ya puedes ejecutar consultas SQL:

Ingresa:

```
SELECT * FROM AGENTS;
```

y obtendras algo como esto:


```
AGENT_CODE    AGENT_NAME    WORKING_AREA      COMMISSION  PHONE_NO      COUNTRY
------------  ------------  --------------  ------------  ------------  ---------
A007          Ramasundar    Bangalore               0.15  077-25814763
A003          Alex          London                  0.13  075-12458969
A008          Alford        New York                0.12  044-25874365
A011          Ravi Kumar    Bangalore               0.15  077-45625874
A010          Santakumar    Chennai                 0.14  007-22388644
A012          Lucida        San Jose                0.12  044-52981425
A005          Anderson      Brisban                 0.13  045-21447739
A001          Subbarao      Bangalore               0.14  077-12346674
A002          Mukesh        Mumbai                  0.11  029-12358964
A006          McDen         London                  0.15  078-22255588
A004          Ivan          Torento                 0.15  008-22544166
A009          Benjamin      Hampshair               0.11  008-22536178

```