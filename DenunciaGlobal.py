from amino import Client, SubClient
import amino

# login
client = Client()
client.login(email='seu-email', password='sua-senha')

# subclient global
subclient = SubClient(comId=None, profile=client.profile, client=client)

# pesquisar usuários pelo nome de usuário ou ID
query = 'nome-de-usuário-ou-id'
users = subclient.search_users(query=query, start=0, size=10).content

if users:
    # obter informações do usuário (apenas como exemplo)
    user_id = users[0].objectId
    user_info = client.get_user_info(user_id=user_id)

    # denunciar o usuário por violar as diretrizes da comunidade
    flag_reason = "Conteúdo impróprio"
    flag_type = amino.types.FlagType.VIOLATION
    client.flag(reason=flag_reason, flagType=flag_type, userId=user_id, objectType=amino.types.ObjectType.USER)

    print(f"Usuário {user_info.nickname} denunciado com sucesso!")
else:
    print("Nenhum usuário encontrado com essa consulta de pesquisa.")
