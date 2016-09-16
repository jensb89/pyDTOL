
#define PS_SOLID        0
#define PS_DASH         1
#define PS_DOT          2
#define PS_DASHDOT      3
#define PS_DASHDOTDOT   4

#define COLOR DWORD

HANDLE FAR WINAPI GraphOpen( HDC hDC, LPRECT WinRect, BOOL Grid,
            LPSTR Title, LPSTR xLabel, LPSTR yLabel,
            COLOR clrLabels, COLOR clrTitle, COLOR clrAxes,
            double xMin, double xMax, double xDiv, int xDec,
            double yMin, double yMax, double yDiv, int yDec );

int FAR WINAPI GraphClose(HANDLE h);

int FAR WINAPI GraphDblLine(HANDLE h, double far * X, double far * Y,
                     int count, COLOR clrLine, int Style);

int FAR WINAPI GraphFltLine(HANDLE h, float far * X, float far * Y,
                     int count, COLOR clrLine, int Style);

int FAR WINAPI GraphIntLine(HANDLE h, int far * X, int far * Y,
                     int count, COLOR clrLine, int Style);

int FAR WINAPI GraphLongLine(HANDLE h, long far * X, long far * Y,
                     int count, COLOR clrLine, int Style);

int FAR WINAPI GraphMoveTo(HANDLE h, double X, double Y);

int FAR WINAPI GraphLineTo(HANDLE h, double X, double Y);


int FAR WINAPI GraphBar(HANDLE h, double X, double Y,
   double Width, COLOR clrBar, COLOR clrBorder,
   LPSTR Label, COLOR clrLabel);

void FAR WINAPI GraphToClient(HANDLE h, double X, double Y, POINT * pt);

void FAR WINAPI ClientToGraph(HANDLE h, POINT pt, double *X, double *Y);

int FAR WINAPI GraphIntSignal(HANDLE h, float xstart, float xinc ,
               int far * Y,int count, COLOR clrLine, int Style);

int FAR WINAPI GraphFltSignal(HANDLE h, float xstart, float xinc ,
               float far * Y,int count, COLOR clrLine, int Style);

#define PC_RED    RGB(255,0,0)
#define PC_GREEN  RGB(0,255,0)
#define PC_BLUE   RGB(0,0,255)
#define PC_YELLOW RGB(255,255,0)
#define PC_LTBLUE RGB(0,255,255)
#define PC_VIOLET RGB(255,0,255)
#define PC_WHITE  RGB(255,255,255)
#define PC_BLACK  RGB(0,0,0)

