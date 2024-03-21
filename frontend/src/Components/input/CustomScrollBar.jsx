import { MarginContainer } from "@liro_u/react-components";
import React, { forwardRef, useEffect, useState } from "react";

const CustomScrollBar = forwardRef(
  (
    {
      parentRef,
      childRef,
      backgroundColor,
      ThumbColor,
      minThumbHeight = 20,
      ...content
    },
    ref
  ) => {
    const [scrollPosition, setScrollPosition] = useState(0);
    const [scrollThumbHeight, setScrollThumbHeight] = useState(1);

    const [isDragging, setIsDragging] = useState(false);
    const [initialY, setInitialY] = useState(0);
    const [initialScrollPosition, setInitialScrollPosition] = useState(0);
    const [needRefresh, setNeedRefresh] = useState(0);
    const [visible, setVisible] = useState(true);

    const refresh = () => {
      setNeedRefresh(true);
    };

    useEffect(() => {
      const handleChildScroll = () => {
        if (childRef.current) {
          const scrollTop = childRef.current.scrollTop;
          setScrollPosition(scrollTop);

          if (parentRef.current) {
            parentRef.current.scrollTop = scrollTop;
          }
        }
      };

      if (ref) {
        ref.current = {
          handleChildScroll,
          refresh,
        };
      }
    }, [ref, childRef, parentRef]);

    useEffect(() => {
      if (childRef.current && parentRef.current) {
        const ratio =
          childRef.current.clientHeight / childRef.current.scrollHeight;
        setVisible(ratio !== 1);
        setScrollThumbHeight(
          Math.max(ratio * parentRef.current.clientHeight, minThumbHeight)
        );
      }
      if (needRefresh === true) {
        setNeedRefresh(false);
      }
    }, [childRef, parentRef, minThumbHeight, needRefresh]);

    const handleMouseDown = (e) => {
      e.preventDefault();
      setIsDragging(true);
      setInitialY(e.clientY);
      setInitialScrollPosition(scrollPosition);
    };

    useEffect(() => {
      const handleMouseMove = (e) => {
        if (isDragging) {
          const deltaY = e.clientY - initialY;
          const maxScroll =
            childRef.current.scrollHeight - childRef.current.clientHeight;
          const scrollDelta =
            (deltaY / (parentRef.current.clientHeight - scrollThumbHeight)) *
            maxScroll;
          const newScrollPosition = Math.min(
            Math.max(0, initialScrollPosition + scrollDelta),
            maxScroll
          );
          setScrollPosition(newScrollPosition);
          childRef.current.scrollTop = newScrollPosition;
        }
      };

      const handleMouseUp = () => {
        setIsDragging(false);
      };

      if (isDragging) {
        document.addEventListener("mousemove", handleMouseMove);
        document.addEventListener("mouseup", handleMouseUp);
        return () => {
          document.removeEventListener("mousemove", handleMouseMove);
          document.removeEventListener("mouseup", handleMouseUp);
        };
      }
    }, [
      isDragging,
      childRef,
      initialY,
      initialScrollPosition,
      scrollThumbHeight,
      parentRef,
    ]);

    return (
      <MarginContainer
        style={{
          backgroundColor: backgroundColor,
          borderRadius: "30px",
          opacity: visible ? 1 : 0,
          width: "10px",
          pointerEvents: visible ? "" : "none",
        }}
      >
        <div
          onMouseDown={isDragging ? () => {} : handleMouseDown}
          ref={ref}
          {...content}
          style={{
            cursor: "pointer",
            position: "absolute",
            top:
              childRef.current && parentRef.current
                ? `${
                    (scrollPosition /
                      (childRef.current.scrollHeight -
                        childRef.current.clientHeight)) *
                    (parentRef.current.clientHeight - scrollThumbHeight)
                  }px`
                : 0,
            right: "0px",
            width: "10px",
            height: scrollThumbHeight + "px",
            backgroundColor: ThumbColor,
            borderRadius: "30px",
            outline: "1px solid var(--dark-color)",
          }}
        />
      </MarginContainer>
    );
  }
);

export default CustomScrollBar;
