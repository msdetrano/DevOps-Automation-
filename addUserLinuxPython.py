import subprocess

usuarios = ["devops1", "sre2", "admin3"]

for user in usuarios:
    subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", user])
    subprocess.run(["sudo", "echo", f"{user}:SenhaForte123" , "|", "chpasswd"])
    print(f"Usuário {user} criado com sucesso!")
