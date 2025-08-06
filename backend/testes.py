import pandas as pd

opcao = ""

while(opcao != "exit"):
    print("\nVocê quer dar uma olhada em qual dataset?")
    opcao = input("""Opções:
        cdas;
        distribuicao_cdas;
        inscricoes_canceladas;
        inscricoes_quitadas;
        inscricoes;
        montante_acumulado;
        quantidade_cdas;
        saldo_cdas;\n
Digite "exit" se quiser sair.\n\n""")

    if(opcao == "cdas"):
        df_cdas = pd.read_json("data/cdas.json")
        print(f"""\n\nDIMENSÕES:\n{df_cdas.shape}
        \nCOLUNAS:\n{df_cdas.columns}
        \nTIPO:\n{df_cdas.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_cdas.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_cdas.head()}
        \nINFORMARÇÕES:\n{df_cdas.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_cdas.describe()}""")

    if(opcao == "distribuicao_cdas"):
        df_dist_cdas = pd.read_json("data/distribuicao_cdas.json")
        print(f"""\n\nDIMENSÕES:\n{df_dist_cdas.shape}
        \nCOLUNAS:\n{df_dist_cdas.columns}
        \nTIPO:\n{df_dist_cdas.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_dist_cdas.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_dist_cdas.head()}
        \nINFORMARÇÕES:\n{df_dist_cdas.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_dist_cdas.describe()}""")

    if(opcao == "inscricoes_canceladas"):
        df_ins_can = pd.read_json("data/inscricoes_canceladas.json")
        print(f"""\n\nDIMENSÕES:\n{df_ins_can.shape}
        \nCOLUNAS:\n{df_ins_can.columns}
        \nTIPO:\n{df_ins_can.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_ins_can.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_ins_can.head()}
        \nINFORMARÇÕES:\n{df_ins_can.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_ins_can.describe()}""")

    if(opcao == "inscricoes_quitadas"):
        df_ins_qui = pd.read_json("data/inscricoes_quitadas.json")
        print(f"""\n\nDIMENSÕES:\n{df_ins_qui.shape}
        \nCOLUNAS:\n{df_ins_qui.columns}
        \nTIPO:\n{df_ins_qui.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_ins_qui.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_ins_qui.head()}
        \nINFORMARÇÕES:\n{df_ins_qui.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_ins_qui.describe()}""")

    if(opcao == "inscricoes"):
        df_ins = pd.read_json("data/inscricoes.json")
        print(f"""\n\nDIMENSÕES:\n{df_ins.shape}
        \nCOLUNAS:\n{df_ins.columns}
        \nTIPO:\n{df_ins.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_ins.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_ins.head()}
        \nINFORMARÇÕES:\n{df_ins.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_ins.describe()}""")

    if(opcao == "montante_acumulado"):
        df_mont_acum = pd.read_json("data/montante_acumulado.json")
        print(f"""\n\nDIMENSÕES:\n{df_mont_acum.shape}
        \nCOLUNAS:\n{df_mont_acum.columns}
        \nTIPO:\n{df_mont_acum.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_mont_acum.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_mont_acum.head()}
        \nINFORMARÇÕES:\n{df_mont_acum.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_mont_acum.describe()}""")

    if(opcao == "quantidade_cdas"):
        df_quant = pd.read_json("data/quantidade_cdas.json")
        print(f"""\n\nDIMENSÕES:\n{df_quant.shape}
        \nCOLUNAS:\n{df_quant.columns}
        \nTIPO:\n{df_quant.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_quant.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_quant.head()}
        \nINFORMARÇÕES:\n{df_quant.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_quant.describe()}""")

    if(opcao == "saldo_cdas"):
        df_saldo = pd.read_json("data/saldo_cdas.json")
        print(f"""\n\nDIMENSÕES:\n{df_saldo.shape}
        \nCOLUNAS:\n{df_saldo.columns}
        \nTIPO:\n{df_quant.dtypes}
        \nPRIMEIRAS 5 LINHAS:\n{df_saldo.head()}
        \nÚLTIMAS 5 LINHAS:\n{df_saldo.head()}
        \nINFORMARÇÕES:\n{df_saldo.info(verbose=True, show_counts=True)}
        \nDESCRIBE:\n{df_saldo.describe()}""")