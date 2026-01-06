# Render Deployment Configuration

## Quick Copy-Paste Values

### Environment Variables

Copy these exactly as shown:

```
SECRET_KEY=n+o9fs=45owx&1f4582k$%ycp=r#9b5p*-w23)l-1@#q41b7vv
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```

**Note:** Replace `your-app-name` with your actual Render service name.

---

## Render Configuration Settings

### Basic Settings
- **Name**: `django-task-app` (or your choice)
- **Region**: `Oregon (US West)` (or closest to you)
- **Branch**: `main`
- **Root Directory**: `demoapp` ⚠️ **CRITICAL**
- **Environment**: `Python 3`

### Build & Start Commands
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn demoapp.wsgi --log-file -`

---

## Generate New Secret Key

If you need a new secret key, run:

```bash
python generate_secret_key.py
```

Or use this command:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## After Deployment

1. Go to Shell tab in Render dashboard
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

---

## Your Live URL

After successful deployment, your app will be available at:
`https://your-app-name.onrender.com`

Share this URL with Suman! 🚀

