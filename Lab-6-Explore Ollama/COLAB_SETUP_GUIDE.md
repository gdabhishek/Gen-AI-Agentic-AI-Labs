# Ollama Serving Setup Guide for Google Colab

This guide will help you run the `Ollama_Serving.ipynb` notebook in Google Colab and access your Ollama server through ngrok.

## 📋 Prerequisites

1. **Google Colab Account** - Free tier works fine
2. **GPU Runtime** - Enable GPU in Colab (Runtime → Change runtime type → GPU)
3. **ngrok Account & Authtoken** (Free):
   - Sign up at [ngrok.com](https://ngrok.com)
   - Get your authtoken from the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)

## 🚀 Step-by-Step Instructions

### Step 1: Open the Notebook in Colab

1. Upload `Ollama_Serving.ipynb` to your Google Drive or open it directly in Colab
2. Go to **Runtime → Change runtime type**
3. Select **GPU** as Hardware accelerator
4. Click **Save**

### Step 2: Get Your ngrok Authtoken

1. Visit [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)
2. Copy your authtoken 

### Step 3: Run the Notebook Cells

#### Cell 1: Install Ollama
```python
#install ollama
!curl -fsSL https://ollama.com/install.sh | sh
```
- This installs Ollama on the Colab instance
- Wait for "Install complete" message

#### Cell 2: Download ngrok
```python
#download the tgz/zip ngrok -- file
!wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
```
- Downloads the ngrok binary

#### Cell 3: Extract ngrok
```python
#unzip the tgz
!tar xvzf ngrok-v3-stable-linux-amd64.tgz ngrok
```
- Extracts the ngrok executable

#### Cell 4: Authenticate ngrok (IMPORTANT!)
```python
# Authenticates ngrok with your authtoken
# Replace <ngrok_authtoken> with your actual token from step 2
!./ngrok authtoken YOUR_NGROK_AUTHTOKEN_HERE
```

**⚠️ Important:** Replace `YOUR_NGROK_AUTHTOKEN_HERE` with your actual ngrok authtoken!



#### Cell 5: (Optional) Download Model Separately
This cell is commented out, but you can uncomment it to download a model separately:
```python
#!ollama run llama3:8b
```

#### Cell 6: Start Ollama Server with ngrok Tunnel
```python
#serve the ollama in ngrok with port 11434
!ollama serve & ./ngrok http 11434 --host-header="localhost:11434" --log stdout & sleep 5s && ollama run gemma3:12b
```

This cell does several things:
1. Starts the Ollama server in the background
2. Creates an ngrok tunnel to port 11434
3. Waits 5 seconds for services to start
4. Downloads and runs the `gemma3:12b` model (this will take several minutes on first run)

## 🔗 Finding Your ngrok URL

### Check the Cell Output

After running Cell 6, look in the output for a line like:
```
t=2025-06-07T10:54:22+0000 lvl=info msg="started tunnel" obj=tunnels name=command_line addr=http://localhost:11434 url=https://xxxx-xx-xxx-xxx-xx.ngrok-free.app
```

The `url` value is your ngrok public URL! It will look like:
- `https://xxxx-xx-xxx-xxx-xx.ngrok-free.app`



## ⚠️ Important Notes

1. **Session Duration**: Colab sessions timeout after inactivity. If you lose connection, you'll need to restart the process.

2. **ngrok Free Tier Limits**:
   - URLs expire after each ngrok session restart
   - Limited connection time (usually 2 hours for free tier)
   - You'll get a new URL each time you restart

3. **Model Size**: The `gemma3:12b` model is large (~7GB). Make sure you have enough space and the download may take 5-10 minutes.

4. **First Run**: The first time you run a model, Ollama will download it. Subsequent runs will be faster.

5. **Multiple Requests**: You can share the ngrok URL with others to test your Ollama server, but remember it expires when the Colab session ends.

## 🔧 Troubleshooting

### Issue: ngrok says "No such file or directory"
**Solution**: Make sure you've run Cell 3 (extract ngrok) before Cell 4.

### Issue: ngrok authentication fails
**Solution**: Double-check your authtoken in Cell 4. Make sure there are no extra spaces.

### Issue: Can't find ngrok URL in output
**Solution**: 
1. Scroll through all the output from Cell 6
2. Search for "started tunnel" or "url=https://"
3. Use Method 3 above to extract it programmatically

### Issue: Model download is very slow
**Solution**: This is normal for large models. Be patient - it's downloading several GB.

### Issue: Connection refused when accessing ngrok URL
**Solution**: 
1. Wait a few more seconds after Cell 6 completes
2. Make sure both Ollama and ngrok are running
3. Check the cell output for any error messages

## 📝 Quick Reference

| Service | Local URL | Public URL |
|---------|-----------|------------|
| Ollama API | `http://localhost:11434` | `https://YOUR-NGROK-URL.ngrok-free.app` |
| ngrok Web UI | `http://localhost:4040` | N/A (local only) |

## 🎉 Next Steps

Once you have your ngrok URL, you can:
- Share it with others to test your Ollama server
- Use it in other applications via HTTP requests
- Test different models by changing the model name in API calls
- Build custom applications that interact with your Ollama server

Happy serving! 🚀

