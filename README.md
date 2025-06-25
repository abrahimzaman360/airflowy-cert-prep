# Preparing for Astronomer's Airflow Certification

In this repository, I will be preparing and documenting my journey & Learning for Astronomer's Airflow Certification.

## Setup

- Install Astro CLI:
[Installation Guide](https://www.astronomer.io/docs/astro/cli/install-cli/)

- Note:
Make sure docker/podman is installed on your system.

- Clone this repository:

```bash
git clone https://github.com/abrahimzaman360/airflowy-cert-prep && cd airflowy-cert-prep
```

- Run the following command to start the Airflow environment:

```bash
astro dev {command} 
# replace command with: start for starting airflow, restart for restarting, and stop for stopping airflow or kill for killing airflow environment.
```

- Access the Airflow UI by navigating to `http://localhost:8080` in your web browser.

## For development

- Install uv or init new environment in repo folder:

```bash
uv init && uv pip install -r requirements.txt
```

## Resources

Here are the useful links to Astronomer's Airflow Certification:

- Astronomer's Airflow Certification
[Link to Certification](https://academy.astronomer.io/certification-exam-apache-airflow-3-fundamentals)

- Astronomer's Airflow Learning Path:
[Link to Learning Path](https://academy.astronomer.io/path/airflow-101)

### Author (Single Yet)

Ibrahim Zaman (@abrahimzaman360)  
Email: <abrahimzaman360@proton.me>  
Website: [abrahimzaman360](https://tiles.bio/abrahimzaman360)
