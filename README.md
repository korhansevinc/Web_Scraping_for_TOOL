# WEB SCRAPING:
Dizinde 2 farklı image scraping yapan script bulunmakta.
Bunlardan ilki olan web_scraping.py çalıştığında chrome, eğer otomatize edilmiş olduğunu fark ederse blokluyor.
Genelde her çalıştırmada 40 - 50 tane resim çekebiliyor.
Bundan dolayı web_scraping_undetected.py'de chrome'un farketmemesi ve daha fazla 
    resim indirebilmek için undetected_chromedriver kullanıldı.

# Gereklilikler, Kütüphaneler ve Environment :
Script'in çalışabilmesi için bilgisayarın chrome'unun en güncel versiyonda olduğuna emin olun.
Bunun için Chrome --> Ayarlar --> Chrome Hakkında sekmesine giderek gerekli güncellemeleri otomatik yapabilirsiniz.
Daha sonrasında chrome'u yeniden başlatınız.

ChromeDriver 115.XX ve sonraki versiyonları için chromedriver dokumantasyonunca script uyumludur. Hangi sürüm kullanılıyorsa onun stable
versiyonunu indirin ve script'in olduğu dizine taşıyın.
28.02.2024 tarihinde Güncel olarak Chrome'un 122.0.6261.95 versiyonu kullanılmaktadır. Dizindeki lisans ve exe bu sürüme uygun stable versiyonunkidir.

Kütüphaneler ise ;
urllib, chromedriver, selenium ve undetected_chromedriver yüklemek yeterli olmalı.
Kodun çalıştığı environment'teki pip list aşağıdaki gibidir : 

Package                                  Version
---------------------------------------- --------------------
absl-py                                  2.0.0
accelerate                               0.26.1
aiohttp                                  3.9.3
aiosignal                                1.3.1
airsim                                   1.6.0
altair                                   5.2.0
annotated-types                          0.6.0
anyio                                    4.2.0
asgiref                                  3.7.2
asttokens                                2.4.0
async-timeout                            4.0.3
attrs                                    23.2.0
audioread                                3.0.1
backcall                                 0.2.0
backoff                                  2.2.1
bcrypt                                   4.1.2
blinker                                  1.7.0
build                                    1.0.3
cachetools                               5.3.2
certifi                                  2023.7.22
cffi                                     1.16.0
chardet                                  5.2.0
charset-normalizer                       3.3.1
Chroma                                   0.2.0
chroma-hnswlib                           0.7.3
chromadb                                 0.4.22
chromedriver_installer                   0.0.6
chromedriver-py                          114.0.5735.16
click                                    8.1.7
colorama                                 0.4.6
coloredlogs                              15.0.1
contourpy                                1.1.1
ctransformers                            0.2.27
cupy-cuda117                             10.6.0
cvzone                                   1.6.1
cycler                                   0.12.1
Cython                                   3.0.4
cython-bbox                              0.1.5
dataclasses-json                         0.6.3
decorator                                5.1.1
Deprecated                               1.2.14
diskcache                                5.6.3
distlib                                  0.3.8
distro                                   1.9.0
exceptiongroup                           1.1.3
executing                                2.0.0
faiss-cpu                                1.7.4
fastapi                                  0.109.0
fastrlock                                0.8.2
filelock                                 3.13.1
flatbuffers                              23.5.26
fonttools                                4.43.1
frozenlist                               1.4.1
fsspec                                   2023.12.2
gitdb                                    4.0.11
GitPython                                3.1.40
google-auth                              2.23.3
google-auth-oauthlib                     1.1.0
googleapis-common-protos                 1.62.0
greenlet                                 3.0.3
grpcio                                   1.59.0
h11                                      0.14.0
httpcore                                 1.0.2
httptools                                0.6.1
httpx                                    0.26.0
huggingface-hub                          0.20.3
humanfriendly                            10.0
idna                                     3.4
importlib-metadata                       6.11.0
importlib-resources                      6.1.1
InstructorEmbedding                      1.0.1
ipython                                  8.16.1
jedi                                     0.19.1
Jinja2                                   3.1.3
joblib                                   1.3.2
jsonpatch                                1.33
jsonpointer                              2.4
jsonschema                               4.21.1
jsonschema-specifications                2023.12.1
kiwisolver                               1.4.5
kubernetes                               29.0.0
langchain                                0.1.4
langchain-community                      0.0.17
langchain-core                           0.1.17
langsmith                                0.0.85
lapx                                     0.5.5
lazy_loader                              0.3
librosa                                  0.10.1
llama_cpp_python                         0.2.38
llvmlite                                 0.41.1
Markdown                                 3.5
markdown-it-py                           3.0.0
MarkupSafe                               2.1.3
marshmallow                              3.20.2
matplotlib                               3.8.0
matplotlib-inline                        0.1.6
mdurl                                    0.1.2
mmh3                                     4.1.0
monotonic                                1.6
mpmath                                   1.3.0
msgpack                                  1.0.7
msgpack-python                           0.5.6
msgpack-rpc-python                       0.4.1
multidict                                6.0.4
mypy-extensions                          1.0.0
nltk                                     3.8.1
numba                                    0.58.1
numpy                                    1.24.4
oauthlib                                 3.2.2
onnxruntime                              1.17.0
openai                                   1.10.0
opencv-contrib-python                    4.8.0.74
opencv-python                            4.8.0.74
opentelemetry-api                        1.22.0
opentelemetry-exporter-otlp-proto-common 1.22.0
opentelemetry-exporter-otlp-proto-grpc   1.22.0
opentelemetry-instrumentation            0.43b0
opentelemetry-instrumentation-asgi       0.43b0
opentelemetry-instrumentation-fastapi    0.43b0
opentelemetry-proto                      1.22.0
opentelemetry-sdk                        1.22.0
opentelemetry-semantic-conventions       0.43b0
opentelemetry-util-http                  0.43b0
outcome                                  1.3.0.post0
overrides                                7.7.0
packaging                                23.2
pandas                                   2.1.1
parso                                    0.8.3
pickleshare                              0.7.5
Pillow                                   10.1.0
pip                                      23.3.2
platformdirs                             4.2.0
pluggy                                   1.4.0
pooch                                    1.8.0
posthog                                  3.3.4
prompt-toolkit                           3.0.39
protobuf                                 4.23.4
psutil                                   5.9.6
pulsar-client                            3.4.0
pure-eval                                0.2.2
py-cpuinfo                               9.0.0
pyarrow                                  15.0.0
pyasn1                                   0.5.0
pyasn1-modules                           0.3.0
PyAudio                                  0.2.13
pycparser                                2.21
pydantic                                 2.6.0
pydantic_core                            2.16.1
pydeck                                   0.8.1b0
pygame                                   2.5.2
Pygments                                 2.16.1
pyparsing                                3.1.1
pypdf                                    4.0.1
PyPDF2                                   3.0.1
pypdfium2                                4.26.0
PyPika                                   0.48.9
pyproject-api                            1.6.1
pyproject_hooks                          1.0.0
pyreadline3                              3.4.1
PySocks                                  1.7.1
python-dateutil                          2.8.2
python-dotenv                            1.0.1
pytz                                     2023.3.post1
PyYAML                                   6.0.1
referencing                              0.33.0
regex                                    2023.12.25
requests                                 2.31.0
requests-oauthlib                        1.3.1
rich                                     13.7.0
rpds-py                                  0.17.1
rsa                                      4.9
safetensors                              0.4.2
scikit-learn                             1.4.0
scipy                                    1.11.3
seaborn                                  0.13.0
selenium                                 4.17.2
sentence-transformers                    2.2.2
sentencepiece                            0.1.99
setuptools                               69.0.3
six                                      1.16.0
smmap                                    5.0.1
sniffio                                  1.3.0
sortedcontainers                         2.4.0
soundfile                                0.12.1
soxr                                     0.3.7
SpeechRecognition                        3.10.1
SQLAlchemy                               2.0.25
stack-data                               0.6.3
starlette                                0.35.1
streamlit                                1.30.0
streamlit-mic-recorder                   0.0.4
sympy                                    1.12
tenacity                                 8.2.3
tensorboard                              2.15.0
tensorboard-data-server                  0.7.1
termcolor                                2.3.0
thop                                     0.1.1.post2209072238
threadpoolctl                            3.2.0
tokenizers                               0.15.1
toml                                     0.10.2
tomli                                    2.0.1
toolz                                    0.12.1
torch                                    1.13.0+cu117
torchaudio                               0.13.0+cu117
torchvision                              0.14.0+cu117
tornado                                  6.4
tox                                      4.12.1
tqdm                                     4.66.1
traitlets                                5.11.2
transformers                             4.37.2
trio                                     0.24.0
trio-websocket                           0.11.1
typer                                    0.9.0
typing_extensions                        4.9.0
typing-inspect                           0.9.0
tzdata                                   2023.3
tzlocal                                  5.2
ultralytics                              8.1.9
undetected-chromedriver                  3.5.5
urllib3                                  2.0.7
uvicorn                                  0.27.0.post1
validators                               0.22.0
virtualenv                               20.25.0
watchdog                                 3.0.0
watchfiles                               0.21.0
wcwidth                                  0.2.8
webdriver-manager                        4.0.1
websocket-client                         1.7.0
websockets                               12.0
Werkzeug                                 3.0.0
wrapt                                    1.16.0
wsproto                                  1.2.0
yarl                                     1.9.4
zipp                                     3.17.0


# Nasıl Kullanılır ? 

terminalde şu şekilde çağrılabilir : < python dosyasının adı > < görsel adedi > < gorselin context'i / aratilmasi istenilen metin.>
(< ve > isaretleri gerekenleri birbirinden ayırmak için kullanıldı. Çağırırken dikkate almayın.)
# Örnek kullanımlar : 
```bash
python web_scraping_undetected.py 20 cats
```
python web_scraping_undetected.py 20 cats
(Çoğul olunca da bir fark olmayacak, boşuklu - boşluksuz direkt stringi kullanabiliyoruz.)
python web_scraping_undetected.py 50 lord of the rings
```bash
python web_scraping_undetected.py 50 lord of the rings
```