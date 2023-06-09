#Carlos Alberto (nº matricula: 202303732091)

import sqlite3




def cadastrar_funcionario():
cpf = entry_cpf.get()
nome = entry_nome.get()
telefone = entry_telefone.get()
turno = entry_turno.get()
equipe = entry_equipe.get()




conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()




cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_funcionario (cpf INTEGER, nome TEXT, telefone TEXT, turno TEXT, equipe TEXT)")
cursor.execute("INSERT INTO cadastro_funcionario VALUES (?, ?, ?, ?, ?)", (cpf, nome, telefone, turno, equipe))




conn.commit()
conn.close()




entry_cpf.delete(0, tk.END)
entry_nome.delete(0, tk.END)
entry_telefone.delete(0, tk.END)
entry_turno.delete(0, tk.END)
entry_equipe.delete(0, tk.END)




def cadastrar_ferramenta():
cd_ferramenta = entry_cd_ferramenta.get()
des_ferramenta = entry_des_ferramenta.get()
fb = entry_fb.get()
vts = entry_vts.get()
pt = entry_pt.get()
tm = entry_tm.get()
un = entry_un.get()
tpf = entry_tpf.get()
mf = entry_mf.get()




conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()




cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_ferramenta (cd_ferramenta TEXT, des_ferramenta TEXT, fb TEXT, vts TEXT, pt TEXT, tm TEXT, un TEXT, tpf TEXT, mf TEXT)")
cursor.execute("INSERT INTO cadastro_ferramenta VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (cd_ferramenta, des_ferramenta, fb, vts, pt, tm, un, tpf, mf))




conn.commit()
conn.close()




entry_cd_ferramenta.delete(0, tk.END)
entry_des_ferramenta.delete(0, tk.END)
entry_fb.delete(0, tk.END)
entry_vts.delete(0, tk.END)
entry_pt.delete(0, tk.END)
entry_tm.delete(0, tk.END)
entry_un.delete(0, tk.END)
entry_tpf.delete(0, tk.END)
entry_mf.delete(0, tk.END)




def consultar_funcionario():
cpf = entry_consulta_cpf.get()
nome_equipe = entry_consulta_nome_equipe.get()




conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()




if cpf:
cursor.execute("SELECT * FROM cadastro_funcionario WHERE cpf=?", (cpf,))
elif nome_equipe:
cursor.execute("SELECT * FROM cadastro_funcionario WHERE equipe=?", (nome_equipe,))
else:
# Caso não seja fornecido CPF nem nome da equipe, retorna todos os registros
cursor.execute("SELECT * FROM cadastro_funcionario")




results = cursor.fetchall()




# Exibe os resultados em uma janela separada
results_window = tk.Toplevel(janela)
results_window.title("Resultados da Consulta")




for i, row in enumerate(results):
for j, value in enumerate(row):
label = tk.Label(results_window, text=str(value))
label.grid(row=i, column=j)




conn.close()




def consultar_ferramenta():
cd_ferramenta = entry_consulta_cd_ferramenta.get()




conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()




if cd_ferramenta:
cursor.execute("SELECT * FROM cadastro_ferramenta WHERE cd_ferramenta=?", (cd_ferramenta,))
else:
# Caso não seja fornecido o código da ferramenta, retorna todos os registros
cursor.execute("SELECT * FROM cadastro_ferramenta")




results = cursor.fetchall()




# Exibe os resultados em uma janela separada
results_window = tk.Toplevel(janela)
results_window.title("Resultados da Consulta")




for i, row in enumerate(results):
for j, value in enumerate(row):
label = tk.Label(results_window, text=str(value))
label.grid(row=i, column=j)




conn.close()




def show_funcionario_screen():
frame_ferramenta.pack_forget()
frame_consulta.pack_forget()
frame_funcionario.pack()




def show_ferramenta_screen():
frame_funcionario.pack_forget()
frame_consulta.pack_forget()
frame_ferramenta.pack()




def show_consulta_screen():
frame_funcionario.pack_forget()
frame_ferramenta.pack_forget()
frame_consulta.pack()




janela = tk.Tk()
janela.title('Seleção de Cadastro')
janela.geometry('400x500')
janela.resizable(False, False)




btn_funcionario = tk.Button(janela, text='Cadastro de Funcionário', command=show_funcionario_screen)
btn_funcionario.pack(pady=10)




btn_ferramenta = tk.Button(janela, text='Cadastro de Ferramenta', command=show_ferramenta_screen)
btn_ferramenta.pack(pady=10)




btn_consulta = tk.Button(janela, text='Consulta', command=show_consulta_screen)
btn_consulta.pack(pady=10)




# Cadastro de Funcionário
frame_funcionario = tk.Frame(janela)




label_cpf = tk.Label(frame_funcionario, text='CPF:')
label_cpf.grid(row=0, column=0, sticky=tk.W)
entry_cpf = tk.Entry(frame_funcionario)
entry_cpf.grid(row=0, column=1)




label_nome = tk.Label(frame_funcionario, text='Nome:')
label_nome.grid(row=1, column=0, sticky=tk.W)
entry_nome = tk.Entry(frame_funcionario)
entry_nome.grid(row=1, column=1)




label_telefone = tk.Label(frame_funcionario, text='Telefone:')
label_telefone.grid(row=2, column=0, sticky=tk.W)
entry_telefone = tk.Entry(frame_funcionario)
entry_telefone.grid(row=2, column=1)




label_turno = tk.Label(frame_funcionario, text='Turno:')
label_turno.grid(row=3, column=0, sticky=tk.W)
entry_turno = tk.Entry(frame_funcionario)
entry_turno.grid(row=3, column=1)




label_equipe = tk.Label(frame_funcionario, text='Equipe:')
label_equipe.grid(row=4, column=0, sticky=tk.W)
entry_equipe = tk.Entry(frame_funcionario)
entry_equipe.grid(row=4, column=1)




btn_cadastrar_funcionario = tk.Button(frame_funcionario, text='Cadastrar', command=cadastrar_funcionario)
btn_cadastrar_funcionario.grid(row=5, column=0, columnspan=2, pady=10)




# Cadastro de Ferramenta
frame_ferramenta = tk.Frame(janela)




label_cd_ferramenta = tk.Label(frame_ferramenta, text='Código da Ferramenta:')
label_cd_ferramenta.grid(row=0, column=0, sticky=tk.W)
entry_cd_ferramenta = tk.Entry(frame_ferramenta)
entry_cd_ferramenta.grid(row=0, column=1)




label_des_ferramenta = tk.Label(frame_ferramenta, text='Descrição da Ferramenta:')
label_des_ferramenta.grid(row=1, column=0, sticky=tk.W)
entry_des_ferramenta = tk.Entry(frame_ferramenta)
entry_des_ferramenta.grid(row=1, column=1)




label_fb = tk.Label(frame_ferramenta, text='FB:')
label_fb.grid(row=2, column=0, sticky=tk.W)
entry_fb = tk.Entry(frame_ferramenta)
entry_fb.grid(row=2, column=1)




label_vts = tk.Label(frame_ferramenta, text='VTS:')
label_vts.grid(row=3, column=0, sticky=tk.W)
entry_vts = tk.Entry(frame_ferramenta)
entry_vts.grid(row=3, column=1)




label_pt = tk.Label(frame_ferramenta, text='PT:')
label_pt.grid(row=4, column=0, sticky=tk.W)
entry_pt = tk.Entry(frame_ferramenta)
entry_pt.grid(row=4, column=1)




label_tm = tk.Label(frame_ferramenta, text='TM:')
label_tm.grid(row=5, column=0, sticky=tk.W)
entry_tm = tk.Entry(frame_ferramenta)
entry_tm.grid(row=5, column=1)




label_un = tk.Label(frame_ferramenta, text='UN:')
label_un.grid(row=6, column=0, sticky=tk.W)
entry_un = tk.Entry(frame_ferramenta)
entry_un.grid(row=6, column=1)




label_tpf = tk.Label(frame_ferramenta, text='TPF:')
label_tpf.grid(row=7, column=0, sticky=tk.W)
entry_tpf = tk.Entry(frame_ferramenta)
entry_tpf.grid(row=7, column=1)




label_mf = tk.Label(frame_ferramenta, text='MF:')
label_mf.grid(row=8, column=0, sticky=tk.W)
entry_mf = tk.Entry(frame_ferramenta)
entry_mf.grid(row=8, column=1)




btn_cadastrar_ferramenta = tk.Button(frame_ferramenta, text='Cadastrar', command=cadastrar_ferramenta)
btn_cadastrar_ferramenta.grid(row=9, column=0, columnspan=2, pady=10)




# Consulta
frame_consulta = tk.Frame(janela)




label_consulta_cpf = tk.Label(frame_consulta, text='CPF:')
label_consulta_cpf.grid(row=0, column=0, sticky=tk.W)
entry_consulta_cpf = tk.Entry(frame_consulta)
entry_consulta_cpf.grid(row=0, column=1)




label_consulta_nome_equipe = tk.Label(frame_consulta, text='Nome da Equipe:')
label_consulta_nome_equipe.grid(row=1, column=0, sticky=tk.W)
entry_consulta_nome_equipe = tk.Entry(frame_consulta)
entry_consulta_nome_equipe.grid(row=1, column=1)




btn_consultar_funcionario = tk.Button(frame_consulta, text='Consultar Funcionário', command=consultar_funcionario)
btn_consultar_funcionario.grid(row=2, column=0, columnspan=2, pady=10)




label_consulta_cd_ferramenta = tk.Label(frame_consulta, text='Código da Ferramenta:')
label_consulta_cd_ferramenta.grid(row=3, column=0, sticky=tk.W)
entry_consulta_cd_ferramenta = tk.Entry(frame_consulta)
entry_consulta_cd_ferramenta.grid(row=3, column=1)




btn_consultar_ferramenta = tk.Button(frame_consulta, text='Consultar Ferramenta', command=consultar_ferramenta)
btn_consultar_ferramenta.grid(row=4, column=0, columnspan=2, pady=10)




btn_voltar = tk.Button(janela, text='Voltar', command=janela.destroy)
btn_voltar.pack(pady=10)




frame_funcionario.pack()
janela.mainloop()


