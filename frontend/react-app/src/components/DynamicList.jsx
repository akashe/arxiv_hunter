import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import ExpandableText from "./ExpandableText";
import SearchBar from "./SearchBar";
import Loading from "./Loading"

function Main() {
  const [arxivData, setArxivData] = useState([])
  const [searchResults, setSearchResults] = useState([])
  const [loading, setLoading] = useState(true)

  async function fetchUsers() {
    try {
      setLoading(true) // Set loading to true before fetching data
      const { data } = await axios.get("http://127.0.0.1:8000/recommend", {
        params: {
          query: localStorage.getItem("preferences"),
        },
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${localStorage.getItem("appToken")}`,
        },
      })
      console.log(data)
      setArxivData(data)
      setLoading(false) // Set loading to false when fetching is done
    } catch (error) {
      console.error(error)
    }
  }
  useEffect(() => {
    fetchUsers()
  }, [])
  return (
    <div>
      <SearchBar setSearchResults={setSearchResults} />(
      <main className="min-h-screen flex flex-col flex-grow my-40">
        {searchResults.length > 0 ? (
          loading ? (
            <Loading />
          ) : (
            searchResults.map((data) => {
              return (
                <div
                  key={data?.id}
                  className="text-start mx-4 mt-4 p-3 bg-gradient-to-bl from-white via-white to bg-blue-50 border-blue-50 border-2 rounded-md shadow-lg">
                  <p className="mb-1 text-base font-semibold text-black">{data?.title}</p>
                  <p className="text-sm text-black">
                    <ExpandableText title={data?.summary}></ExpandableText>
                  </p>
                  <div className="flex justify-center">
                    <Link
                      to={data?.id}
                      target="_blank">
                      <button className="bg-slate-100 rounded-full h-10 w-10 mr-2 hover:bg-slate-200 flex justify-center items-center">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          strokeWidth={1.5}
                          stroke="currentColor"
                          className="w-6 h-6 flex justify-center items-center">
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418"
                          />
                        </svg>
                      </button>
                    </Link>
                    <Link
                      to={data?.pdf_link}
                      target="_blank">
                      <button className="bg-slate-100 rounded-full h-10 w-10 mr-2 hover:bg-slate-200 flex justify-center items-center">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          strokeWidth={1.5}
                          stroke="currentColor"
                          className="w-6 h-6">
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"
                          />
                        </svg>
                      </button>
                    </Link>
                  </div>
                </div>
              )
            })
          )
        ) : loading ? (
          <Loading />
        ) : (
          arxivData.map((data) => {
            return (
              <div
                key={data?.id}
                className="text-start mx-4 mt-4 p-3 bg-gradient-to-bl from-white via-white to bg-blue-50 border-blue-50 border-2 rounded-md shadow-lg">
                <p className="mb-1 text-base font-semibold text-black">{data?.title}</p>
                <p className="text-sm text-black">
                  <ExpandableText title={data?.summary}></ExpandableText>
                </p>
                <div className="flex justify-center">
                  <Link
                    to={data?.id}
                    target="_blank">
                    <button className="bg-slate-100 rounded-full h-10 w-10 mr-2 hover:bg-slate-200 flex justify-center items-center">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        strokeWidth={1.5}
                        stroke="currentColor"
                        className="w-6 h-6 flex justify-center items-center">
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418"
                        />
                      </svg>
                    </button>
                  </Link>
                  <Link
                    to={data?.pdf_link}
                    target="_blank">
                    <button className=" bg-slate-100 rounded-full h-10 w-10 mr-2 hover:bg-slate-200 flex justify-center items-center">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        strokeWidth={1.5}
                        stroke="currentColor"
                        className="w-6 h-6">
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"
                        />
                      </svg>
                    </button>
                  </Link>
                </div>
              </div>
            )
          })
        )}
      </main>
      )
    </div>
  )
}

export default Main;
