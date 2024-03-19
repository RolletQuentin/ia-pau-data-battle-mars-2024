import {
  CenterContainer,
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useEffect, useRef, useState } from "react";

const CustomScrollbar = () => {
  const [scrollPosition, setScrollPosition] = useState(0);
  const [scrollThumbHeight, setScrollThumbHeight] = useState(1);
  const parentRef = useRef(null);
  const childRef = useRef(null);

  const handleChildScroll = () => {
    const scrollTop = childRef.current.scrollTop;
    setScrollPosition(scrollTop);

    if (parentRef.current) {
      parentRef.current.scrollTop = scrollTop;
    }
  };

  useEffect(() => {
    if (childRef.current && parentRef.current) {
      setScrollThumbHeight(
        (childRef.current.clientHeight / childRef.current.scrollHeight) *
          parentRef.current.clientHeight
      );
    }
  }, [childRef, parentRef]);

  return (
    <MarginContainer>
      <CenterContainer>
        <VBox gap="100px">
          <Text text={scrollPosition} style={{ position: "fixed" }} />
          <HBox justifyContent="center">
            <ColorRect style={{ width: "10px", position: "relative" }}>
              <div
                style={{
                  position: "absolute",
                  top: childRef.current
                    ? `${
                        (scrollPosition / childRef.current.scrollHeight) * 100
                      }%`
                    : 0,
                  right: "0",
                  width: "10px",
                  height: scrollThumbHeight + "px",
                  backgroundColor: "#888",
                }}
              />
            </ColorRect>
            <ColorRect backgroundColor={"blue"}>
              <div
                style={{
                  width: "200px",
                  height: "300px",
                  border: "1px solid #ccc",
                  overflow: "hidden",
                  position: "relative",
                }}
                ref={parentRef}
              >
                <div
                  style={{
                    height: "500px",
                    overflowY: "scroll",
                    marginRight: "-20px", // Adjust for scrollbar width
                  }}
                  onScroll={handleChildScroll}
                  ref={childRef}
                >
                  {Array.from({ length: 40 }).map((_, index) => (
                    <div
                      key={index}
                      style={{
                        padding: "10px",
                      }}
                    >
                      Item {index + 1}
                    </div>
                  ))}
                </div>
              </div>
            </ColorRect>
          </HBox>
        </VBox>
      </CenterContainer>
    </MarginContainer>
  );
};

export default CustomScrollbar;
