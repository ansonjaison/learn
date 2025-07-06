# page.js

```
import Image from "next/image";

export default function Home() {
  return (
    <main className="bg-black text-white">
      {/* Hero Section */}
      <section className="h-screen flex flex-col justify-center items-center px-6 sm:px-12">
        <Image
          src="/profile.jpg"
          alt="Anson's profile photo"
          width={150}
          height={150}
          className="rounded-full mb-6 object-cover"
        />
        <h1 className="text-4xl sm:text-6xl font-bold text-center mb-4">
          Hello, I’m <span className="text-green-500">Anson Jaison</span>
        </h1>
        <p className="text-center text-lg sm:text-xl max-w-xl text-gray-300">
          A student exploring tech, design, and stories that connect people.
        </p>
        <button className="mt-6 bg-green-500 hover:bg-green-600 text-black font-medium px-6 py-2 rounded-full transition">
          Let’s Connect →
        </button>
      </section>

      {/* About Me Section */}
      <section className="h-screen flex flex-col justify-center items-center px-6 sm:px-12 bg-[#111]">
        <h2 className="text-3xl sm:text-4xl font-semibold mb-6 text-green-500">
          About Me
        </h2>
        <div className="max-w-2xl text-center space-y-4 text-lg text-gray-300">
          <p>
            I'm Anson — a final-year BTech student passionate about technology,
            design, and the ideas that bring people together.
          </p>
          <p>
            I love learning by building, and I’m always exploring the
            intersection of code, creativity, and meaningful user experiences.
          </p>
          <p>
            I’m currently trying out different tools and technologies, slowly
            carving out my own path in the world of tech.
          </p>
        </div>
      </section>

      {/* Tools Section */}
      <section className="h-screen flex flex-col justify-center items-center px-6 sm:px-12 bg-black">
        <h2 className="text-3xl sm:text-4xl font-semibold mb-6 text-green-500">
          Tools I Use
        </h2>
        <div className="flex flex-wrap justify-center gap-6 text-lg text-gray-300">
          <span className="bg-[#1a1a1a] px-4 py-2 rounded-full">HTML</span>
          <span className="bg-[#1a1a1a] px-4 py-2 rounded-full">CSS</span>
          <span className="bg-[#1a1a1a] px-4 py-2 rounded-full">JavaScript</span>
          <span className="bg-[#1a1a1a] px-4 py-2 rounded-full">React</span>
          <span className="bg-[#1a1a1a] px-4 py-2 rounded-full">Next.js</span>
          <span className="bg-[#1a1a1a] px-4 py-2 rounded-full">GitHub</span>
          <span className="bg-[#1a1a1a] px-4 py-2 rounded-full">Tailwind CSS</span>
        </div>
      </section>

      {/* Footer Section */}
      <footer className="h-screen flex flex-col justify-center items-center px-6 sm:px-12 bg-[#111]">
        <h2 className="text-2xl sm:text-3xl font-semibold text-center mb-2">
          Let’s <span className="text-green-500">Connect</span>
        </h2>
        <p className="text-gray-400 mb-4">ansonjaison@outlook.in</p>
        <div className="flex gap-6">
          <a
            href="https://github.com/ansonjaison"
            target="_blank"
            rel="noopener noreferrer"
            className="text-green-500 hover:underline"
          >
            GitHub
          </a>
          <a
            href="https://linkedin.com/in/anson-jaison"
            target="_blank"
            rel="noopener noreferrer"
            className="text-green-500 hover:underline"
          >
            LinkedIn
          </a>
        </div>
      </footer>
    </main>
  );
}

```

# Folder Organization

![image](https://github.com/user-attachments/assets/b74631f3-eed4-4401-9441-a964dca42e69)


# Preview

![screencapture-localhost-3000-2025-07-06-11_07_06](https://github.com/user-attachments/assets/9133ba98-a101-4272-a4ea-13924654a9f7)
