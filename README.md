## Hello

```python
import json


class Junlin:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __str__(self):
        return json.dumps(self.__dict__, indent=2, ensure_ascii=False)


me = Junlin(
    first_name="Liu",
    last_name="Junlin",
    website="Domain.Hack",
    github="https://github.com/NoCLin",
    education="Zhejiang University / Software Engineering",
    skills=["Python", "JavaScript", "Java"],
    hobbies=[i for i in "💻🏃📷🏸🎮"],
)
me.__dict__["website"] = f"http://{me.first_name}.{me.last_name[:4]}.{me.last_name[4:]}".lower()

print(me)

assert me.__str__() == """
{
  "first_name": "Liu",
  "last_name": "Junlin",
  "website": "http://liu.junl.in",
  "github": "https://github.com/NoCLin",
  "education": "Zhejiang University / Software Engineering",
  "skills": [
    "Python",
    "JavaScript",
    "Java"
  ],
  "hobbies": [
    "💻",
    "🏃",
    "📷",
    "🏸",
    "🎮"
  ]
}

""".strip()

```

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=noclin)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=noclin&hide=ipynb,html&layout=compact)
