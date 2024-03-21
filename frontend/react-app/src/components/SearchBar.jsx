import { useState } from "react"
import axios from "axios" // Import axios or any other library you're using for API requests

function SearchBar({ setSearchResults }) {
  const [searchTerm, setSearchTerm] = useState("")
  const [arxivData, setArxivData] = useState([])

  const handleSearch = async () => {
    console.log("searched")
    console.log(searchTerm)
    try {
      const { data } = await axios.get("http://127.0.0.1:8000/recommend", {
        params: {
          query: searchTerm,
        },
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${localStorage.getItem("appToken")}`,
        },
      })
      console.log(data)
      setArxivData(data)
      setSearchResults(data)
    } catch (error) {
      console.error(error)
    }
  }

  return (
    <div className="fixed top-16 bg-gradient-to-r from-blue-200 via-purple-200 to-lime-200 left-0 right-0 z-10 h-24 flex items-center justify-center">
      <div className="relative flex items-center w-full max-w-[800px] min-w-min">
        <input
          type="text"
          className="w-full mx-4 px-8 pr-14 py-5 font-medium shadow-lg text-2xl rounded-full bg-white text-black placeholder:font-light placeholder:text-slate-300 focus:outline-none focus:ring-2 focus:ring-black focus:ring-opacity-100"
          placeholder="Try searching here"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={1.5}
          stroke="black"
          className="w-10 h-10 absolute right-7 top-1/2 transform -translate-y-1/2 cursor-pointer"
          onClick={handleSearch}>
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
          />
        </svg>
      </div>
    </div>
  )
}

export default SearchBar
