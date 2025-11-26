import os
import requests

# Get Your API Key From https://html2pdf.app/
# Replace YOUR_API_KEY_HERE with your key
API_KEY = "YOUR_API_KEY_HERE" 
BASE_PATH = "/storage/emulated/0/"

def get_html_from_input():
    """Get HTML content by pasting code"""
    print("    Paste your HTML code")
    print("    Type 'END' on new line after you pasted the code")
    print("    Let's go:")   
    html_lines = []
    while True:
        line = input("    ")
        # Check if the line (case-insensitive) is "END"
        if line.strip().upper() == "END":
            break
        html_lines.append(line)
    
    # Remove any empty lines at the beginning that might be from pasting
    while html_lines and not html_lines[0].strip():
        html_lines.pop(0)
    
    return "\n".join(html_lines)

def get_html_from_file():
    """Get HTML content from file upload"""
    print("\n    📁 File Upload")
    print("    ──────────────")
    print("    Enter the path to your HTML file:")
    print("    Example: Documents/myfile.html")
    print("    Example: Downloads/newfile.html")
    print()
    
    relative_path = input("    📂 File path: ").strip()
    
    # Combine with base path
    file_path = os.path.join(BASE_PATH, relative_path)
    
    # Customize upload process
    print(f"\n    🔄 Uploading: {os.path.basename(file_path)}")
    
    if not os.path.exists(file_path):
        print("    ❌ File not found!")
        print(f"    💡 Full path: {file_path}")
        print("    💡 Please check the path and try again")
        return None
    
    if not file_path.lower().endswith('.html'):
        print("    ⚠️  Warning: File doesn't have .html extension")
        continue_anyway = input("    Continue anyway? (y/N): ").strip().lower()
        if continue_anyway != 'y':
            return None
    
    try:
        file_size = os.path.getsize(file_path)
        print(f"    📊 File size: {file_size:,} bytes")
        print("    ⏳ Reading file content...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("    ✅ File uploaded successfully!")
        return content
        
    except UnicodeDecodeError:
        print("    ❌ Error: Cannot read file (encoding issue)")
        print("    💡 Try saving the file as UTF-8")
        return None
    except Exception as e:
        print(f"    ❌ Error reading file: {e}")
        return None

def main():
    print("    📄 HTML to PDF Converter")
    print("    😍 Brought to you by Trader Abba")
    print("    👉 Follow me @TraderAbba")
    print("    ================================\n")
    
    # Check API key
    if API_KEY == "YOUR_API_KEY_HERE":
        print("    ❌ Please set your API key first!")
        print("    🔑 Get free key from: https://html2pdf.app/")
        return
    
    # Choose input method
    print("    Choose input method:")
    print("    ┌─────────────────────┐")
    print("    │  A) 📝 Paste HTML code  │")
    print("    │  B) 📁 Upload HTML file │")
    print("    └─────────────────────┘")
    print()
    
    choice = input("    Enter your choice (A/B): ").strip().upper()
    
    html_content = ""
    
    if choice == 'A':
        html_content = get_html_from_input()
    elif choice == 'B':
        html_content = get_html_from_file()
    else:
        print("    ❌ Invalid choice! Please enter A or B")
        return
    
    if not html_content or not html_content.strip():
        print("    ❌ No HTML content provided!")
        return
    
    # Get filename
    print("\n    💾 Save PDF As")
    print("    ──────────────")
    filename = input("    Enter PDF filename [document]: ").strip()
    if not filename:
        filename = "document"
    
    # Remove .pdf if user included it, then add it properly
    if filename.lower().endswith('.pdf'):
        filename = filename[:-4]
    
    filename = filename + '.pdf'
    
    # Convert HTML to PDF
    print(f"\n    🔄 Converting to {filename}...")
    
    try:
        response = requests.post(
            "https://api.html2pdf.app/v1/generate",
            json={'html': html_content, 'apiKey': API_KEY},
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        if response.status_code == 200:
            # Save to Download folder
            download_path = "/storage/emulated/0/Download"
            file_path = os.path.join(download_path, filename)
            
            with open(file_path, "wb") as f:
                f.write(response.content)
            
            # Format the output with proper borders
            file_size_str = f"{len(response.content):,} bytes"
            filename_display = filename.ljust(20)
            file_size_display = file_size_str.ljust(15)
            
            print("    ✅ Conversion Successful!")
            print("    ┌─────────────────────────────────────────────┐")
            print(f"    │ 📁 {filename_display} │")
            print(f"    │ 📊 {file_size_display} │")
            print(f"    │ 📍 {download_path} │")
            print("    └─────────────────────────────────────────────┘")
            
        elif response.status_code == 401:
            print("    ❌ Invalid API Key")
            print("    💡 Get your free key from: https://html2pdf.app/")
        else:
            print(f"    ❌ API Error {response.status_code}: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("    ❌ No internet connection")
    except requests.exceptions.Timeout:
        print("    ❌ Request timed out")
    except Exception as e:
        print(f"    ❌ Error: {e}")

if __name__ == "__main__":
    main()