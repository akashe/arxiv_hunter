import React, { useState, useEffect } from 'react';

function TodaysPaper() {
    const [papers, setPapers] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/get_today_papers', {
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${localStorage.getItem("appToken")}`,
        },
      }) // Modify this URL to your actual API endpoint
            .then(response => response.json())
            .then(data => setPapers(data))
            .catch(error => console.error('Error fetching papers:', error));
    }, []);

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="mt-6">
                {papers.map(paper => (
                    <div key={paper.id} className="p-4 bg-white shadow-lg rounded-lg my-5">
                        <h3 className="text-lg font-bold">{paper.title}</h3>
                        <p className="text-gray-600 mt-2">{paper.pdf_link}</p>
                        <p className="text-gray-600 mt-2">{paper.summary}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default TodaysPaper;


// src/components/TodayPapers.jsx
// import axios from "axios";
// import React, { useState, useEffect } from 'react';
// import DynamicList from './DynamicList'; // Reusing your DynamicList component
//
//
// const papers_raw = await fetch("http://127.0.0.1:8000/get_today_papers", {
//         headers: {
//           Accept: "application/json",
//           Authorization: `Bearer ${localStorage.getItem("appToken")}`,
//         },
//       });
// console.log(papers_raw)
//     if (!papers) {
//         throw new Error('Network response was not ok');
//     }
//
// const TodaysPapers = () => {
//     const [papers, setPapers] = useState([]);
//     const [loading, setLoading] = useState(true);

//     useEffect(() => {
//         getTodayPapersLocally()  // Assume you have this API method implemented
//             .catch(error => {
//                 console.error("Failed to fetch today's papers:", error);
//                 setLoading(false);
//             });
//     }, []);

//     return (
//         <div className="p-4">
//             <h1 className="text-lg font-bold mb-4">Today's Papers</h1>
//             <ul>
//                 {papers.map(paper => (
//                     <li key={paper.id} className="mb-2">
//                         <a href={paper.link} target="_blank" rel="noopener noreferrer">{paper.title}</a>
//                     </li>
//                 ))}
//             </ul>
//         </div>
//     );
// };
//
// export default TodaysPapers;
