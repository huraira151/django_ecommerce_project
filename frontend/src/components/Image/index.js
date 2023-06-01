import React from "react"

const Image = ({ className, onClick, src, alt }) => {
  return (
    <img
      src={src}
      alt={alt}
      className={className}
      onClick={onClick}
    />
  )
}

export default Image
