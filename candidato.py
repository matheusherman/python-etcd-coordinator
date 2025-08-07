import sys
import time
import etcd3

#MATHEUS HERMAN BERNARDIM ANDRADE

key = 'lider'
candidato = sys.argv[1]
etcd = etcd3.client()

print(f"Candidato {candidato}")

while True:
    print("Tentando Liderança")
    resposta = etcd.get(key)

    if resposta[0] is not None:
        lider = resposta[0].decode('utf-8')

        if lider != candidato:
            print(f"{lider} é o líder...")
            etcd.watch(key)

            while True:
                resposta = etcd.get(key)
                if resposta[0] is None or resposta[0].decode('utf-8') != lider:
                    break
                time.sleep(1)
            print(f"{lider} finalizou.")
    else:
        print(f'{candidato}: Sou líder')
        etcd.put(key, candidato)
        print("Tecle CTRL + C para terminar")

        try:
            while True:
                for _ in range(3):
                    print(".", end='', flush=True)
                    time.sleep(1)
                print()

        except KeyboardInterrupt:
            print("\nFim")
            etcd.delete(key)
            sys.exit(0)
