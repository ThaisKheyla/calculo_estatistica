library(tidyverse)

#importar os CSVs que a gente gerou no Python
processos <- read_csv("processos.csv")
processos_io <- read_csv("processos_io.csv")

#dar uma olhada geral nos dados
summary(processos)    
summary(processos_io) 

# ver os 5 processos que mais estão usando CPU
top_cpu <- processos %>%
  arrange(desc(cpu_percent)) %>%
  head(5)
print("Top 5 processos por CPU:")
print(top_cpu)

#ver os 5 processos que mais usam memória
top_mem <- processos %>%
  arrange(desc(memoria_rss)) %>%
  head(5)
print("Top 5 processos por memória:")
print(top_mem)

#ver os 5 processos que mais fazem leitura de disco
top_io <- processos_io %>%
  arrange(desc(bytes_lidos)) %>%
  head(5)
print("Top 5 processos por bytes lidos:")
print(top_io)

# gráfico de threads por processo
ggplot(processos_io, aes(x = nome, y = threads)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  coord_flip() +
  labs(title = "Número de threads por processo",
       x = "Processo",
       y = "Threads")

#gráfico de bytes lidos por processo, só pra ter outra visão
ggplot(processos_io, aes(x = nome, y = bytes_lidos)) +
  geom_bar(stat = "identity", fill = "darkgreen") +
  coord_flip() +
  labs(title = "Bytes lidos por processo",
       x = "Processo",
       y = "Bytes lidos")

# dá pra fazer várias coisas com esses dados :D
# como por exemplo ver quem tá consumindo mais CPU, mais memória, quem tá lendo mais do disco
# ver se processos com mais threads usam mais recurso
# fazer gráficos pra ver visualmente o que tá pesado no sistema
