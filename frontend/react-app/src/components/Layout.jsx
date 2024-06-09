import React from 'react';
import Header from './Header';

const Layout = ({ children }) => {
  return (
    <div>
      <Header />
      <div className="pt-16"> {/* Added padding to account for the fixed header */}
        {children}
      </div>
    </div>
  );
};

export default Layout;
