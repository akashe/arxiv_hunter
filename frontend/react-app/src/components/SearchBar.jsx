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
    <div className="fixed top-16 mt-4 mx-6 left-0 right-0 z-10 h-16 flex items-center justify-center">
      <div className="relative flex items-center w-full max-w-[800px] min-w-min">
        <input
          type="text"
          className="w-full px-8 py-5 font-semibold text-2xl rounded-full bg bg-slate-300 text-gray-800 focus:outline-none focus:ring-2 focus:ring-gray-800 focus:ring-opacity-100"
          placeholder="Search here..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={2.5}
          stroke="gray"
          className="w-10 h-10 absolute right-4 top-1/2 transform -translate-y-1/2 cursor-pointer"
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
