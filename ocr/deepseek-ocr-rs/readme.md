deepseek-ocr-rs readme
----------------------


```bash
# install rust runtime
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
git clone https://github.com/TimmyOVO/deepseek-ocr.rs.git app
cd app 
cargo fetch
cargo run -p deepseek-ocr-cli --release -- --help

# cargo build with cuda support
cargo build --locked --release -p deepseek-ocr-cli --features cuda
cargo build --locked --release -p deepseek-ocr-server --features cuda

# using cpu
cargo run -p deepseek-ocr-server --release -- \
  --host 0.0.0.0 --port 8000 \
  --device cpu --max-new-tokens 512

# using gpu
cargo run -p deepseek-ocr-server --release --features cuda -- \
  --host 0.0.0.0 --port 8000 \
  --device cuda --dtype f16

# model location: ~/.cache/deepseek-ocr/modles/deepseek-ocr/*.*

target/release/deepseek-ocr-server --host 0.0.0.0 --port 8000 --device cuda --dtype f16
```