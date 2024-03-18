import { Link } from "react-router-dom"
function NotFoundPage() {
  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gradient-to-tr from-white to-blue-200">
      <h1 className="text-6xl mb-5 text-red-500 text-center">404!!!</h1>
      <h1 className="text-6xl mb-5 text-center">not found :(</h1>
      <Link
        className=" text-white font-bold bg-black px-4 py-2 rounded-full"
        to="/">
        Go to Home
      </Link>
    </div>
  )
}

export default NotFoundPage
