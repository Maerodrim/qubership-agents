# Руководство по локальной разработке и настройке

Инструкция по подготовке рабочего окружения для работы с проектом `qubership-envgene`.

---

## 📋 Предварительные требования

- **Python**: 3.10+ (рекомендуется 3.11)
- **Git**
- **Docker** / Podman (для запуска локальных тестов и сборки образов)
- **Make**

---

## 🛠️ Настройка окружения

1. **Клонирование репозитория и форка**:
   ```bash
   git clone https://github.com/Netcracker/qubership-envgene.git
   cd qubership-envgene
   git remote add fork https://github.com/Maerodrim/qubership-envgene.git
   ```

2. **Создание и активация виртуального окружения**:
   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .venv\Scripts\Activate.ps1
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Установка зависимостей**:
   ```bash
   pip install -U pip setuptools wheel
   pip install -r dependencies/requirements.txt
   pip install -r dependencies/requirements-dev.txt
   ```

4. **Установка pre-commit хуков**:
   ```bash
   pre-commit install
   ```

---

## 🧪 Запуск тестов и линтеров

### 1. BDD Тесты (Cucumber / Behave):
```bash
# Запуск всех BDD тестов:
pytest cucumber_tests/
# или
behave cucumber_tests/
```

### 2. Проверка типов и линтинг:
```bash
# Pyright / Mypy:
pyright

# Линтинг кода:
flake8 modules/
black --check modules/
```

### 3. Линтинг документации:
```bash
markdownlint docs/ *.md
```
