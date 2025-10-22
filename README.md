# Reconhecimento Facial

Aplicativo simples de detecção facial em Python. O programa abre a câmera do dispositivo e, ao detectar um rosto, desenha um retângulo azul ao redor.

Observação: este README foi gerado/ajustado usando os arquivos reais presentes no repositório — o script principal é `ReconhecimentoFacial.py` e o cascade do OpenCV (`haarcascade_frontalface_default.xml`) já está incluso no repositório.

## Estrutura principal do repositório
- ReconhecimentoFacial.py — script principal que abre a webcam e faz a detecção em tempo real.  
- haarcascade_frontalface_default.xml — modelo Haar Cascade usado para detectar faces (fornecido junto ao projeto).  
- history.py, history_internal.py — utilitários presentes no repositório (histórico/ajuda interna).  
- db/ — diretório para armazenamento.
- defaults/, onlinehelp/ — pastas de configuração/ajuda.  
- template.py — arquivo auxiliar pequeno.  
- .ropeproject, spyder.ini, spyder.ini.bak, spyder.lock, langconfig, workingdir — arquivos/arquivos de configuração do ambiente/editor.

## Requisitos
- Python 3.6+ (recomenda-se Python 3.8+)
- Pacotes Python:
  - opencv-python
  - numpy

Instalação rápida das dependências:
```bash
pip install opencv-python numpy
```

(Se você usa um ambiente virtual: python -m venv .venv && source .venv/bin/activate || .venv\Scripts\activate)

## Como executar
Na raiz do repositório, execute:
```bash
python ReconhecimentoFacial.py
```

Comportamento esperado:
- A janela da webcam será aberta.
- Ao detectar um rosto, o programa desenha um retângulo azul ao redor da face.

## Observações técnicas (resumo)
- O projeto usa detecção baseada em Haar Cascades (arquivo XML incluido).
- Fluxo típico: captura de frames com cv2.VideoCapture -> conversão para escala de cinza -> detecção com CascadeClassifier -> desenho de retângulos com cv2.rectangle -> exibição com cv2.imshow.

## Troubleshooting
- Erro ao importar cv2: verifique se instalou `opencv-python` no mesmo ambiente Python.
- Webcam não abre: tente alterar o índice da câmera (0, 1, …) ou libere permissões do sistema.
- Detecções falsas/omissões: ajuste parâmetros do cascade (scaleFactor, minNeighbors, minSize) dentro do script.

## Contribuição
Sinta-se à vontade para abrir issues ou pull requests. Sugestões úteis:
- Adicionar README (este arquivo), requirements.txt e LICENSE.
- Exemplo de argumentos e instruções de execução específicas.
- Capturas de tela ou GIFs demonstrando o funcionamento.

## Contato
Autor: romilsonx (veja o perfil no GitHub).
