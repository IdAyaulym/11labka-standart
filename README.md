# devops-ci-lab

Простая практическая работа: DevOps и Continuous Integration (часть 1)

[![CI](https://github.com/YOUR-USERNAME/devops-ci-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR-USERNAME/devops-ci-lab/actions)

## Описание проекта
Пример простого Python-проекта с unit-тестами и CI на GitHub Actions.
Цель: показать базовый CI-процесс: установка зависимостей, запуск тестов, сборка Docker-образа.

## Как запустить локально
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Сборка Docker-образа
```bash
docker build -t devops-ci-lab:latest .
docker run --rm devops-ci-lab:latest
```

## Стандарты и этапы DevOps
| Этап DevOps | Инструмент / Артефакт | Соответствующий стандарт | Цель стандарта |
|-------------|-----------------------|--------------------------|----------------|
| Continuous Integration | GitHub Actions | ISO/IEC 12207 | Определение процессов жизненного цикла ПО, автоматизация сборки |
| Configuration Management | Git | IEEE 828 | Управление конфигурациями и версиями |
| Testing | pytest | ISO/IEC 25010 / IEEE 829 | Контроль качества и тестирование ПО |
| Deployment / Containerization | Docker | ITIL v4 / ISO/IEC 25010 | Надёжность, доступность сервисов, переносимость |

## Вывод
CI автоматизирует проверку качества кода и повышает надёжность поставки. Контейнеризация обеспечивает воспроизводимость окружения и упрощает деплой.
"# 11labka-standart" 
