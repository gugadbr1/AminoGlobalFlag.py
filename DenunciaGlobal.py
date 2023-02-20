from amino import Client, SubClient
import amino

# login
client = Client()
client.login(email='seu-email', password='sua-senha')

# subclient global
subclient = SubClient(comId=None, profile=client.profile, client=client)

# pesquisar usu�rios pelo nome de usu�rio ou ID
query = 'nome-de-usu�rio-ou-id'
users = subclient.search_users(query=query, start=0, size=10).content

if users:
    # obter informa��es do usu�rio (apenas como exemplo)
    user_id = users[0].objectId
    user_info = client.get_user_info(user_id=user_id)

    # denunciar o usu�rio por violar as diretrizes da comunidade
    flag_reason = "Conte�do impr�prio"
    flag_type = amino.types.FlagType.VIOLATION
    client.flag(reason=flag_reason, flagType=flag_type, userId=user_id, objectType=amino.types.ObjectType.USER)

    print(f"Usu�rio {user_info.nickname} denunciado com sucesso!")
else:
    print("Nenhum usu�rio encontrado com essa consulta de pesquisa.")
