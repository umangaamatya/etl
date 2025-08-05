# Spotify Dataset ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline for processing Spotify music dataset from Kaggle. This project downloads, extracts, and processes Spotify track data from 1921-2020 containing 600k+ tracks.

## 🎵 Project Overview

This ETL pipeline is designed to:
- **Extract** Spotify dataset from Kaggle
- **Transform** the data (implementation in progress)
- **Load** the processed data to a destination (implementation in progress)

## 📁 Project Structure

```
etl/
├── main.py                 # Main ETL pipeline orchestrator
├── extract/
│   └── execute.py          # Data extraction module
├── transform/
│   └── transform.py        # Data transformation module (TODO)
├── load/
│   └── load.py            # Data loading module (TODO)
└── README.md              # This file
```

## 🚀 Features

### Extraction Module (`extract/execute.py`)
- Downloads Spotify dataset from Kaggle as a ZIP file
- Extracts ZIP contents to specified directory
- Fixes JSON dictionary format for artist data
- Converts `dict_artists.json` to JSONL format (`fixed_da.json`)
- Automatic cleanup of temporary files

### Pipeline Orchestrator (`main.py`)
- Coordinates the entire ETL process
- Error handling and logging
- Modular design for easy maintenance

## 📋 Requirements

- Python 3.x
- `requests` library for HTTP downloads
- Standard libraries: `os`, `sys`, `zipfile`, `json`

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd etl
```

2. Install required dependencies:
```bash
pip install requests
```

## 📖 Usage

### Running the Complete ETL Pipeline

```bash
python3 main.py /path/to/extraction/directory
```

Example:
```bash
python3 main.py /Users/amatyaumanga/Workspace/etl
```

### Running Individual Modules

#### Extract Only
```bash
python3 extract/execute.py /path/to/extraction/directory
```

#### Transform (Implementation needed)
```bash
python3 transform/transform.py
```

#### Load (Implementation needed)
```bash
python3 load/load.py
```

## 📊 Data Source

- **Dataset**: Spotify Dataset 1921-2020, 600k+ Tracks
- **Source**: [Kaggle](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks)
- **Format**: ZIP file containing multiple data files including artist dictionaries and track information

## 🔄 Pipeline Process

1. **Extract Phase**:
   - Downloads ZIP file from Kaggle
   - Extracts all files to specified directory
   - Processes `dict_artists.json` to JSONL format
   - Cleans up temporary files

2. **Transform Phase** (TODO):
   - Data cleaning and validation
   - Feature engineering
   - Data type conversions
   - Aggregations and calculations

3. **Load Phase** (TODO):
   - Database insertion
   - File output
   - API uploads
   - Data warehouse loading

## 🛠️ Development Status

- ✅ **Extract**: Fully implemented
- ⚠️ **Transform**: Implementation needed
- ⚠️ **Load**: Implementation needed

## 📝 File Outputs

After running the extraction:
- `fixed_da.json`: Artist dictionary in JSONL format
- Other Spotify dataset files (tracks, features, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Implement transform/load modules
4. Add tests
5. Submit a pull request

## 📜 License

This project is open source. Please check the dataset license on Kaggle for data usage terms.

## 🐛 Error Handling

The pipeline includes comprehensive error handling:
- Network connectivity issues
- File system permissions
- Data format validation
- Resource cleanup on failures

## 🔮 Future Enhancements

- [ ] Implement data transformation logic
- [ ] Implement data loading to various destinations
- [ ] Add configuration file support
- [ ] Add logging framework
- [ ] Add unit tests
- [ ] Add data validation and quality checks
- [ ] Add support for incremental updates
- [ ] Add Docker containerization

## 📞 Support

For issues or questions, please create an issue in the repository or contact me at amatyaumanga@gmail.com
