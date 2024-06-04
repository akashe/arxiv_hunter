
function TabsComponent() {
    return (
        <div className="bg-gray-100 py-4">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-center space-x-4">
                    <a href="/" className="px-3 py-2 text-sm font-medium text-gray-700 hover:text-gray-900">
                        Home
                    </a>
                    <a href="/today" className="px-3 py-2 text-sm font-medium text-gray-700 hover:text-gray-900">
                        Today's Paper
                    </a>
                </div>
            </div>
        </div>
    );
}

export default TabsComponent;
