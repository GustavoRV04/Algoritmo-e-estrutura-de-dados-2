from pilha import Pilha

class TorreHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        
        self.haste_a = Pilha()
        self.haste_b = Pilha()
        self.haste_c = Pilha()
        
        self.hastes = {
            'A': self.haste_a,
            'B': self.haste_b,
            'C': self.haste_c
        }
        
        self.inicializar_jogo()
        self.movimentos = 0
    
    def inicializar_jogo(self):
        print(f"\n=== Inicializando Torre de Hanoi com {self.num_discos} discos ===")
        
        for disco in range(self.num_discos, 0, -1):
            self.haste_a.push(disco)
        
        print("\nEstado inicial:")
        self.exibir_estado()
    
    def mover_disco(self, origem, destino):
        haste_origem = self.hastes[origem]
        haste_destino = self.hastes[destino]
        
        if haste_origem.esta_vazia():
            print(f"❌ Movimento inválido: Haste {origem} está vazia!")
            return False
        
        if not haste_destino.esta_vazia():
            if haste_origem.peek() > haste_destino.peek():
                print(f"❌ Movimento inválido: Não pode colocar disco {haste_origem.peek()} sobre disco {haste_destino.peek()}!")
                return False
        
        disco = haste_origem.pop()
        haste_destino.push(disco)
        
        self.movimentos += 1
        print(f"✅ Movimento {self.movimentos}: Disco {disco} de {origem} para {destino}")
        
        return True
    
    # def resolver_automatico(self, n, origem='A', destino='C', auxiliar='B'):
    #     if n == 1:
    #         self.mover_disco(origem, destino)
    #         self.exibir_estado()
    #     else:
    #         self.resolver_automatico(n-1, origem, auxiliar, destino)
    #         self.mover_disco(origem, destino)
    #         self.exibir_estado()
    #         self.resolver_automatico(n-1, auxiliar, destino, origem)
    
    def exibir_estado(self):
        print("\n--- Estado Atual das Hastes ---")
        print(f"Haste A: {self.haste_a.itens}")
        print(f"Haste B: {self.haste_b.itens}")
        print(f"Haste C: {self.haste_c.itens}")
        print("-" * 35)
    
    def jogo_completo(self):
        return (self.haste_a.esta_vazia() and 
                self.haste_b.esta_vazia() and 
                self.haste_c.tamanho() == self.num_discos)
    
    def resolver_interativo(self):
        print("\n🎮 Modo Interativo - Resolva você mesmo!")
        print("Digite movimentos no formato: A B (move disco de A para B)")
        print("Digite 'sair' para terminar")
        print("Digite 'auto' para resolver automaticamente")
        
        while not self.jogo_completo():
            self.exibir_estado()
            
            entrada = input("\nSeu movimento (ex: A C): ").strip().upper()
            
            if entrada == 'SAIR':
                break
            elif entrada == 'AUTO':
                print("\n🤖 Resolvendo automaticamente...")
                discos_restantes = self.haste_a.tamanho()
                if discos_restantes > 0:
                    self.resolver_automatico(discos_restantes)
                break
            
            try:
                partes = entrada.split()
                if len(partes) == 2:
                    origem, destino = partes[0], partes[1]
                    if origem in self.hastes and destino in self.hastes:
                        self.mover_disco(origem, destino)
                    else:
                        print("❌ Use apenas as letras A, B, C para as hastes")
                else:
                    print("❌ Formato inválido! Use: A B")
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        if self.jogo_completo():
            print(f"\n🎉 PARABÉNS! Você completou a Torre de Hanoi em {self.movimentos} movimentos!")
            movimento_minimo = 2**self.num_discos - 1
            print(f"📊 Movimentos mínimos possíveis: {movimento_minimo}")
        
        self.exibir_estado() 