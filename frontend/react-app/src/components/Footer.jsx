function Footer ()
{
    return <div className="fixed bottom-0 left-0 right-0 z-10 h-16 bg-white flex items-center justify-center mx-8">
        <div className="relative flex items-center w-full max-w-[800px]">
            <input type="text" className="w-full px-4 py-2 rounded-full bg-slate-300 text-gray-700 focus:outline-none focus:ring-2 focus:ring-slate-800 focus:ring-opacity-60" placeholder="Search here..."/>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 absolute right-4 top-1/2 transform -translate-y-1/2">
                <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
            </svg>

        </div>

    </div>
}

export default Footer