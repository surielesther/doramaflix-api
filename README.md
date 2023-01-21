# Doramaflix API

Repositório do projeto Doramaflix, que se inspira na plataforma Netflix.
Dorama nada mais é do que uma espécie de série de origem asiática, produzida na Coréia do Sul, Japão, China e Tailândia. O termo “dorama” vem da pronúncia de “drama” em japonês. Essas novelas podem ter vários segmentos, como a comédia, romance, aventura e até mesmo terror.

### Conteúdo
1. [Stack do projeto](#stack)
2. [Descrição das branches](#descriçao)
3. [Endpoints da API](#endpoints)
   1. [Rotas de Usuário](#user)
   2. [Rotas de Doramas](#dorama)
   3. [Rotas de Reviews](#reviews)

## Stack do projeto <a name="stack"></a>

Nesse projeto foi utilizada a linguagem de back-end Python com Django Rest Framework. Outras libs e ferramentas que foram utilizadas estão no arquivo 'requirements.txt'. O tipo de banco de dados utilizado foi o PostgresSQL.

## Descrição das branches <a name="descriçao"></a>

`main` - É a branch principal do projeto.

`develop` - Essa branch contém o código de pré-produção, onde farei as features e testes.


## Endpoints da API <a name="endpoints"></a>

Os endpoints estão divididos de acordo com seus contextos e suas models.

### User <a name="user">

#### Criando um usuário

```
http://localhost:8000/api/users/
```
Modelo da requisição:
```
{
  "username": "exemplo",
  "email": "exemplo@email.com",
  "password": "123456",
  "is_admin":false
}
```
  Resposta:
  `201 CREATED`
```
{
  "id": 1,
  "username": "exemplo",
  "email": "exemplo@email.com",
  "created_at": "2023-01-19T20:28:48.491745Z",
  "is_admin": false,
  "is_superuser": true
}
```
  
  #### Fazendo login

```
http://localhost:8000/api/users/login/
```
Modelo da requisição:
```
{
	"username": "matheus",
	"password": "1234"
}
```
  Resposta:
  `200 OK`
```
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDc2NDk4OCwiaWF0IjoxNjc0MTYwMTg4LCJqdGkiOiI1YmU1ODA3NDBiNzI0Zjg5YmFjZjM4OGQxOGY0YzY5NSIsInVzZXJfaWQiOjE0fQ.zK92xwT5ldN1zvvdtErzlOoHsylAr6-G8wm14ZZ3JkU",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MjE0MTg4LCJpYXQiOjE2NzQxNjAxODgsImp0aSI6IjgyMTIwNTU4YjQ1ODRjNGFiMjgyNDc5OTA4NThhNjI0IiwidXNlcl9pZCI6MTR9.wc7_o2AH_EkbZkbg6G65MEgxIu1sYGCeHthvgnkS6b0"
  }
```

### Dorama <a name="dorama">
  
### Reviews <a name="reviews">
